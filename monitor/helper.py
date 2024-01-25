import paramiko
import monitor.data as md
import pandas as pd

def connect_ssh_client():
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect(md.HOST_NAME,
                   username = md.USER,
                   password = md.PWD)
    return client

def get_start_id(client, file_name):
    with client.open_sftp() as sftp_client:
        with sftp_client.open(file_name) as remote_file:
            for id, line in enumerate(remote_file):
                if 'time/iter' in line:
                    legend = line.split()[1:-1]
                    start_id = id
                    break
    return [legend, start_id]

def fetch_residue(client, file_name, start_id, n_eqns):
    residue = []
    with client.open_sftp() as sftp_client:
        with sftp_client.open(file_name) as remote_file:
            for id, line in enumerate(remote_file):
                if id <= start_id:
                    continue
                else:
                    A = line.split()
                    if(len(A) != n_eqns+3):
                        continue
                    if 'flow' in line:
                        continue
                    residue.append(A[1:n_eqns+1])
                    if 'converged' in line:
                        break
            last_id = id

    return [last_id, pd.DataFrame(residue)]

def get_residue(file_name):
    client = connect_ssh_client()
    [legend, start_id] = get_start_id(client, file_name)
    [last_id, residue] = fetch_residue(client, file_name, start_id, len(legend))
    return [residue, legend, last_id]

def convert_float(res):
    for i in res.columns:
        res.iloc[:, i] = res.iloc[:, i].astype(float)
    return res

def extract_scale(res):
    max_res = []
    min_res = []
    for i in res.columns:
        max_res.append(max(res.iloc[:, i]))
        min_res.append(min(res.iloc[:, i]))
        
    max_res = max(max_res)
    min_res = [i for i in min_res if i != 0]
    min_res = min(min_res)

    X = [0, max(res.index), int(max(res.index)/5), 'linear']
    Y = [min_res/10, max_res*10, 1e-2, 'log']

    return [X, Y]

