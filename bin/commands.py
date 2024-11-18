from bin.cluster import get_file_path
from bin.monitor import animate_plot

    
def _monitor():
    ouput_file_path = get_file_path()

    if ouput_file_path != False:
        converged = animate_plot(ouput_file_path)
