import pandas as pd 

from lib.helper import connect_ssh_client, ssh_command
from lib.data import USER


def collate_duplicates(df):
    job_ID = df['JOB_ID'].values
    node_num = []
    jid = []
    jname = []
    user = []
    load = []
    status = []
    date = []
    time = []
    n_cores = []
    
    df_add = pd.DataFrame()
    for i in list(set(job_ID)):
        df_raw = df.query(f"JOB_ID == '{i}'")
        if len(df_raw) == 1:
            node_num.append(i)
            n_cores.append(df_raw['N_CORES'].values[0])
        else:
            N_nodes = ",".join(list(df_raw['NODE_NUM'].values))
            node_num.append(N_nodes)
            total_cores = sum([int(i) for i in list(df_raw['N_CORES'].values)])
            n_cores.append(total_cores)

        jid.append(i)
        jname.append(df_raw['JOB_NAME'].values[0])
        user.append(df_raw['USER'].values[0])
        load.append(df_raw['LOAD'].values[0])
        status.append(df_raw['STATUS'].values[0])
        date.append(df_raw['DATE'].values[0])
        time.append(df_raw['TIME'].values[0])

    df_add['NODE_NUM'] = node_num
    df_add['JOB_ID'] = jid
    df_add['JOB_NAME'] = jname
    df_add['LOAD'] = load
    df_add['USER'] = user
    df_add['STATUS'] = status
    df_add['DATE'] = date
    df_add['TIME'] = time
    df_add['N_CORES'] = n_cores

    return df_add


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


def get_file_path():
    client = connect_ssh_client()

    # LIST ALL CASES RUNNING UNDER USER
    running_cases = get_cluster_status(client)
    my_cases = running_cases.query(f"USER == '{USER}'")
    final_cases = collate_duplicates(my_cases)
    # print(my_cases.head)
    
    if len(final_cases) > 0:
        print(f"\nCURRENTLY RUNNING CASES FOR {USER}:\n\n")
        print("-"*100)
        print("OPTION\tJOB_ID\tJOB_NAME\tDATE\t\tTIME\t\tNODE_NUM\tN_CORES")
        print("-"*100)
        
        for index, row in final_cases.iterrows():
            print(f"{index+1}\t{row['JOB_ID']}\t{row['JOB_NAME']}\t\t{row['DATE']}\t{row['TIME']}\t{row['NODE_NUM']}\t\t{row['N_CORES']}")

        print("-"*100)
        
        option = input("\nEnter which of the above cases to monitor or Enter 'q' to quit(OPTION):\t")

        if option == 'q':
            return False
        else:
            # MAKE SELECTION BASED ON JOB ID
            job_ID = my_cases["JOB_ID"].iloc[int(option)-1]

            # FIND FILE NAME OF OUTPUT AND ADDRESS BASED ON JOB ID
            output = ssh_command(client, f"qstat -explain c -j {job_ID}")[1:]
            folder = output[11].split(':')[1].strip() 
            file_name = output[19].split('/')[1].strip()
            file_path = f"{folder}/{file_name}"
            
            return file_path
    else:
        print(f"CURRENTLY NO CASE IS RUNNING FOR {USER}\n")
        return False
