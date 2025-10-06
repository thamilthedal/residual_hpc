import paramiko
import lib.data as md
import pandas as pd
import time
import numpy as np

def connect_ssh_client():
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.connect(md.HOST_NAME, username=md.USER, password=md.PWD)
    return client


def ssh_command(client, command):
    stdin, stdout, stderr = client.exec_command(command)
    out_list = stdout.readlines()
    return out_list


def write_file(file_address):
    with open(file_address, 'w') as f:
        f.write("residue\n")


def append_file(file_address, line):
    with open(file_address, 'a') as f:
        f.writelines(" ".join(line))

def get_remote_file_contents(client, file_name):
    with client.open_sftp() as sftp_client:
        with sftp_client.open(file_name) as remote_file:
            remote_file_contents = remote_file.readlines()

    return remote_file_contents

def get_start_id(client, file_name):
    remote_file_contents = get_remote_file_contents(client, file_name)
    for id, line in enumerate(remote_file_contents):
        if 'time/iter' in line:
            legend = line.split()[1:-1]
            start_id = id
            return [legend, start_id]
    return [0, 0]


def fetch_residue(client, file_name, start_id, legend, n_eqns):
    residue = []
    last_id = 0
    
    remote_file_contents = get_remote_file_contents(client, file_name)
    for id, line in enumerate(remote_file_contents):
        if id <= start_id:
            continue
        else:
            A = line.split()
            if 'Total Transcript' in line and id == len(line)-1:
                last_id = "Over!"
                break
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
    residue["over"] = True if last_id == "Over!" else False

    return residue


def get_residue(file_name):
    count = 0
    while(True):
        client = connect_ssh_client()
        [legend, start_id] = get_start_id(client, file_name)
        if start_id == 0:
            if count == 0:
                # print("Iterations are not started.", end="\t")
                count += 1
            else:
                print(".", end="\t")
            time.sleep(15)
        else:
            break
    residue = fetch_residue(client, file_name, start_id, legend, len(legend))
    return residue

def get_data(file_name):
    client = connect_ssh_client()
    remote_file_contents = get_remote_file_contents(client, file_name)
    data = remote_file_contents[3:-1]
    raw_data = [i.strip().split(" ") for i in data]
<<<<<<< HEAD
=======

>>>>>>> c6e8c448a0ce357543bef8feced64bfd083ef68b
    raw_data = np.array(raw_data)
    x_data = raw_data[:, 0]
    y_data = raw_data[:, 1]

    variable = [x_data.astype(np.float64), y_data.astype(np.float64)]

    return variable



def extract_scale(res):
    max_res = res.iloc[:, :-2].max().max()
    min_res = res.replace(0, float('nan')).iloc[:, :-2].min().min()

    X = [0, max(res.index), int(max(res.index) / 5), 'linear']
    Y = [min_res / 100, max_res * 100, 1e-2, 'log']

    return [X, Y]


def get_eqns(file_name):
    res = get_residue(file_name)
    return [len(res.columns) - 2, res.columns[:-2]]

def write_code(code):
    with open("./.code", "w") as file:
        file.write(f"{code}")

def get_code():
    with open("./.code", "r") as file:
        code = int(file.readlines()[0])
        return code

def print_header(heading: str)-> None:

    character = '-'
    offset = 5

    length = len(heading) + (2*offset)

    print(character*length)
    print(" "*offset + heading.upper() + " "*offset)
    print(character*length)

def get_report_values(file_name):
    pass

