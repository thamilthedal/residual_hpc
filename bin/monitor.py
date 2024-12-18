import sys 
import time 
import numpy as np
import pandas as pd 
import matplotlib.animation as animation

from lib.data import fig, ax, plt, RES_MARKERS
import lib.helper as mh
from lib.helper import write_code, get_code, print_header
from lib.data import CONV_CRITERIA

# Generating Residual Data
def data_gen(output_file_path):
    return mh.get_residue(output_file_path)


def update(frame, output_file_path, ax, line_list):

    # for each frame, update the data stored on each artist and update the axis scale.
    residue = data_gen(output_file_path)
    X, Y = mh.extract_scale(residue)
    ax.set_xlim(X[0], X[1]+X[2])
    ax.set_xscale(X[3])
    ax.set_ylim(Y[0], Y[1]+Y[2])
    ax.set_yscale(Y[3])
    fig.canvas.draw()
    for n, i in enumerate(residue.columns[:-2]):
        line_list[f"line_{n + 1}"].set_data(residue.index, residue[i])
    ax.hlines(xmin = X[0], xmax = X[1]+X[2], y = CONV_CRITERIA, linestyle = 'dashed', linewidth=2, colors = 'red')
    
    if residue["conv"].all():
        ax.text(X[0]+0.5*X[2], Y[1]/100,"Converged!", fontsize=25, color = 'red')
        write_code(13)

    if residue["over"].all():
        ax.text(X[0]+0.5*X[2], Y[1]/100,"Over!", fontsize=25, color = 'red')
        write_code(3)

    return (line_list)


def animate_residue_plot(output_file_path):

    print_header(f"Monitoring output file: {output_file_path}")

    # Initializing Plot
    fig.suptitle(output_file_path, fontsize=16)
    n_eqns, legend = mh.get_eqns(output_file_path)
    line_list = {}
    for i in range(n_eqns):
        line_list["line_" + str(i + 1)], = ax.plot([], [], RES_MARKERS[i], label=legend[i])
    ax.legend(ncols=2)

    write_code(1)
    
    # Monitor Plot Frame will refresh at an interval of 15 seconds
    # Number of frames will be equal to number of iterations

    ani = animation.FuncAnimation(fig=fig, func=update, frames=100000, fargs = (output_file_path, ax, line_list), interval=15000)
    plt.show(block=True)
    code = get_code()
    if code == 13:
        print_header("Simulation Converged!")
        return True
    if code == 3:
        print_header("Simulation for given number of iterations got over!")
        return True
    else:
        print_header("Monitor closed before simulation got over!")
        return False

def animate_report_plot(report_file_path):
    pass

