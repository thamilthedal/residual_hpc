import pandas as pd 

from CLI.lib.helper import connect_ssh_client, ssh_command
from CLI.lib.data import USER


def collate_duplicates(df):

    collating_rules = {
        'NODE_NUM': lambda x: ','.join(x.astype(str)),
        'N_CORES': 'sum',
        'JOB_NAME': 'first',
        'USER': 'first',
        'LOAD': 'first',
        'STATUS': 'first',
        'DATE': 'first',
        'TIME': 'first'
    }

    return df.groupby('JOB_ID', as_index=False).agg(collating_rules).sort_values(by=['JOB_ID'])


def get_cluster_status(client):
    out_list = ssh_command(client, "qstat  -f")
    running_cases = []
    for i in out_list[1:]:
        if '-----' in i:
            continue
        if 'compute' in i:
            node_number = i.split()[0].split('-')[-1].split('.')[0]
        else:
            if 'dr' not in i:
                running_cases.append([node_number] + i.split())


    running_cases = pd.DataFrame(running_cases, 
                 columns = 
                 ["NODE_NUM",
                  "JOB_ID", 
                  "LOAD", 
                  "JOB_NAME", 
                  "USER", 
                  "STATUS", 
                  "DATE", 
                  "TIME", 
                  "N_CORES"])

    return running_cases

def get_jobs():
    client = connect_ssh_client()

    # LIST ALL CASES RUNNING UNDER USER
    running_cases = get_cluster_status(client)
    user_cases = running_cases.query(f"USER == '{USER}'")
    processed_cases = collate_duplicates(user_cases)
    client.close()
    return processed_cases


def print_jobs():
    final_cases = get_jobs()

    if len(final_cases) > 0:

        print(f"\nCURRENTLY RUNNING CASES FOR {USER}:\n\n")
        print("-"*100)
        print("OPTION\tJOB_ID\tJOB_NAME\tDATE\t\tTIME\t\tNODE_NUM\tN_CORES")
        print("-"*100)

        for index, row in final_cases.iterrows():
            print(f"{index+1}\t{row['JOB_ID']}\t{row['JOB_NAME']}\t{row['DATE']}\t{row['TIME']}\t{row['NODE_NUM']}\t\t{row['N_CORES']}")
        print("-"*100)
    else:
        print(f"CURRENTLY NO CASE IS RUNNING FOR {USER}\n")

def fetch_out_file_path(job_ID):
    client = connect_ssh_client()
    # FIND FILE NAME OF OUTPUT AND ADDRESS BASED ON JOB ID
    output = ssh_command(client, f"qstat -explain c -j {job_ID}")[1:]
    client.close()
    folder = output[11].split(':')[1].strip() 
    file_name = output[19].split('/')[1].strip()
    file_path = f"{folder}/{file_name}"            
    return file_path


def get_out_file_path():

    final_cases = get_jobs()
    if len(final_cases) > 0:        
        client = connect_ssh_client()
        option = input("\nEnter which of the above cases to monitor or Enter 'q' to quit(OPTION):\t")

        if option == 'q':
            return False
        else:
            # MAKE SELECTION BASED ON JOB ID
            job_ID = final_cases["JOB_ID"].iloc[int(option)-1]

            # FIND FILE NAME OF OUTPUT AND ADDRESS BASED ON JOB ID
            output = ssh_command(client, f"qstat -explain c -j {job_ID}")[1:]
            client.close()
            folder = output[11].split(':')[1].strip() 
            file_name = output[19].split('/')[1].strip()
            file_path = f"{folder}/{file_name}"
            
            return file_path
    else:
        return False

def fetch_report_file_path(job_ID):
    client = connect_ssh_client()
    # FIND FILE NAME OF OUTPUT AND ADDRESS BASED ON JOB ID
    output = ssh_command(client, f"qstat -explain c -j {job_ID}")[1:]
    folder = output[11].split(':')[1].strip()
    command = f"ls {folder}/*.csv"
    output = ssh_command(client, command)
    client.close()
    if len(output) > 0:
        file_path = output[0].strip()
        return file_path
    else:
        print("NO FILES REPORTED!\n")
        return None


def get_report_file_path():
    # Connect to SSH
    client = connect_ssh_client()
    final_cases = get_jobs()
    client = connect_ssh_client()

    if len(final_cases) > 0:        
        option = input("\nEnter which of the above cases to monitor or Enter 'q' to quit(OPTION):\t")

        if option == 'q':
            return False
        else:
            # MAKE SELECTION BASED ON JOB ID
            job_ID = final_cases["JOB_ID"].iloc[int(option)-1]

            # FIND FILE NAME OF OUTPUT AND ADDRESS BASED ON JOB ID
            output = ssh_command(client, f"qstat -explain c -j {job_ID}")[1:]
            folder = output[11].split(':')[1].strip()

            command = f"ls {folder}/*.csv"
            output = ssh_command(client, command)
            client.close()
            if len(output) > 0:
                file_path = output[0].strip()
                return file_path
            else:
                print("NO FILES REPORTED!\n")
                return False
