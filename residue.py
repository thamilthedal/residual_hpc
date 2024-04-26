import monitor.monitor as mm
import sys

def run(file_name):
    mm.start_monitor()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        file_name = input("Enter the filepath to be monitored: ")
        run(file_name)
    else:
        run(sys.argv[1])
