import paramiko
import CLI.data as md
import pandas as pd
import time
import numpy as np
import io
from datetime import datetime

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

def get_remote_file_contents(client, file_name, sampling_data="+1"):
    command = f"tail -n {sampling_data} {file_name}"
    stdin, stdout, stderr = client.exec_command(command)
    return stdout.readlines()

def get_start_id(client, file_name):
    remote_file_contents = get_remote_file_contents(client, file_name)
    for id, line in enumerate(remote_file_contents):
        if 'time/iter' in line:
            legend = line.split()[1:-1]
            start_id = id
            return [legend, start_id]
    return [0, 0]


def parse_value(value_str):
    """Helper function to safely convert a string to a float."""
    try:
        return float(value_str)
    except (ValueError, TypeError):
        return np.nan

def fetch_residue(client, file_name):
    """
    Parses a list of lines to extract all residual data.
    """
    lines_list = get_remote_file_contents(client, file_name, str(md.SAMPLING_DATA))
    all_data_rows = []
    column_headers = ['iter', 'continuity', 'x-velocity', 'y-velocity', 'energy', 'k', 'omega']
    
    # Directly iterate over the list of lines (much faster)
    for line in lines_list:
        if "binary" in line:
            continue
        if "Stabilizing" in line:
            continue
        parts = line.strip().split()

        if len(parts) < 7:
            continue

        try:
            iteration = int(parts[0])
        except ValueError:
            continue

        # print(parts)

        residuals = [parse_value(p) for p in parts[1:7]]
        all_data_rows.append([iteration] + residuals)


    df = pd.DataFrame(all_data_rows, columns=column_headers)

    # print(df.dtypes)

    return df


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
    # residue = fetch_residue(client, file_name, start_id, legend, len(legend))
    residue = fetch_residue(client, file_name)
    return residue

def get_data(file_name):
    client = connect_ssh_client()
    remote_file_contents = get_remote_file_contents(client, file_name)
    data = remote_file_contents[3:-1]
    raw_data = [i.strip().split(" ") for i in data]
    raw_data = np.array(raw_data)
    x_data = raw_data[:, 0]
    y_data = raw_data[:, 1]

    variable = [x_data.astype(np.float64), y_data.astype(np.float64)]

    return variable


def extract_scale(residuals):
    
    # print(residuals.query("iter == iter.max()"))

    iterations = residuals["iter"]
    # print(iterations)
    # print(iterations.max(), iterations.min())
    iter_max = iterations.iloc[-1]
    iter_min = iterations.iloc[0]
    # iter_min = iter_max - (len(iterations)-1)
    iter_step = abs((iter_max - iter_min))/5
    # print(iter_max, iter_min)
    max_iter = np.log10(iter_max)
    min_iter = np.log10(iter_min)
    # print(max_iter, min_iter)
    X = [10**min_iter, 10**max_iter, 1, 'log']

    max_res = residuals.iloc[:, 1:].max().max()
    min_res = residuals.replace(0, float('nan')).iloc[:, 1:-2].min().min()
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

def print_error(heading: str)-> None:

    character = '-'
    offset = 5

    length = len(heading) + (2*offset)

    print(character*length)
    print(" "*offset + heading.upper() + " "*offset)
    print(character*length)


def calculate_eta(start_str):
    now = datetime.now()

    # Convert string to a datetime object for today
    start_time = datetime.strptime(start_str, "%H:%M:%S").replace(
        year=now.year, month=now.month, day=now.day
    )

    elapsed = now - start_time
    elapsed = np.round(elapsed.total_seconds() / 3600, 2)
    return elapsed
