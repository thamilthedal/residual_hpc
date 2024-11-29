import paramiko
import monitor.data as md
import pandas as pd


def connect_ssh_client():
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect(md.HOST_NAME,
                   username=md.USER,
                   password=md.PWD)
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


def fetch_residue(client, file_name, start_id, legend, n_eqns):
    residue = []
    last_id = 0
    with client.open_sftp() as sftp_client:
        with sftp_client.open(file_name) as remote_file:
            for id, line in enumerate(remote_file):
                if id <= start_id:
                    continue
                else:
                    A = line.split()
                    if 'converged' in line:
                        last_id = "Converged!"
                        break
                    if len(A) != n_eqns + 3:
                        continue
                    if bool(set(md.WORDS).intersection(line)):
                        continue
                    residue.append(A[1:n_eqns + 1])
    residue = pd.DataFrame(residue).apply(pd.to_numeric, errors='coerce')
    residue.columns = legend

    residue["conv"] = True if last_id == "Converged!" else False

    return residue


def get_residue(file_name):
    client = connect_ssh_client()
    [legend, start_id] = get_start_id(client, file_name)
    return fetch_residue(client, file_name, start_id, legend, len(legend))


def extract_scale(res):
    max_res = res.iloc[:, :-1].max().max()
    min_res = res.replace(0, float('nan')).iloc[:, :-1].min().min()

    X = [0, max(res.index), int(max(res.index) / 5), 'linear']
    Y = [min_res / 100, max_res * 100, 1e-2, 'log']

    return [X, Y]


def get_eqns(file_name):
    res = get_residue(file_name)
    return [len(res.columns) - 1, res.columns[:-1]]
