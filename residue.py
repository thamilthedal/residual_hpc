import monitor.monitor as mm
import monitor.helper as mh
from lib.plot_utils import plt
import sys

def run(file_name):
    while(True):
        [residual, legend, last_id]= mh.get_residue(file_name)
        print(last_id)
        mm.monitor_residue(file_name, residual, legend)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        file_name = input("Enter the filepath to be monitored: ")
        run(file_name)
    else:
        run(sys.argv[1])
