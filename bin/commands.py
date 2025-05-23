from bin.cluster import print_jobs, get_out_file_path, get_report_file_path
import shutil
from bin.monitor import animate_residue_plot, animate_report_plot

def _jobs():
    print_jobs()

def _monitor():
    output_file_path = get_out_file_path()

    if output_file_path != False:
        converged = animate_residue_plot(output_file_path)

def _file():
    report_file_path = get_report_file_path()

    if report_file_path != False:
        print(report_file_path)
        animate_report_plot(report_file_path)

def _clear_pyc():
    folder_paths = [
                    "./CLI/__pycache__",
                    "./bin/__pycache__",
                    "./lib/__pycache__"
            ]
    for folder in folder_paths:
        shutil.rmtree(folder)

