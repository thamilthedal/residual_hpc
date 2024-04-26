import matplotlib.pyplot as plt
import matplotlib.animation as animation
import monitor.helper as mh
import sys
from monitor.data import fig, ax, RES_MARKERS

n_eqns, legend = mh.get_eqns(sys.argv[1])
line_list = {}
for i in range(n_eqns):
    line_list["line_" + str(i + 1)], = ax.plot([], [], RES_MARKERS[i], label=legend[i])
ax.legend(ncols=2)


def data_gen():
    yield mh.get_residue(sys.argv[1])


def init():
    ax.set_ylim(0.1, 1000)
    ax.set_xlim(0, 1)
    xdata, ydata = [], []
    del xdata[:]
    del ydata[:]
    for i in range(len(line_list)):
        line_list["line_" + str(i + 1)].set_data(xdata, ydata)
    return line_list


def run(residue):
    X, Y = mh.extract_scale(residue)

    ax.set_xlim(X[0], X[1])
    ax.set_xscale(X[3])
    ax.set_ylim(Y[0], Y[1])
    ax.set_yscale(Y[3])
    ax.figure.canvas.draw()

    for n, i in enumerate(residue.columns[:-1]):
        line_list[f"line_{n + 1}"].set_data(residue.index, residue[i])
    ax.hlines(xmin = X[0], xmax = X[1], y = 1e-5, linestyle = 'dashed', linewidth=2, colors = 'red')

    if residue["conv"].all() == True:
        ax.text(X[0]+0.5*X[2], Y[1]/100,"Converged!", fontsize=25, color = 'red')
    return line_list


def start_monitor():
    ani = animation.FuncAnimation(fig, run, data_gen, interval=300, init_func=init,
                                  save_count=100)
    plt.show()


def main():
    print("Hello World!")


if __name__ == '__main__':
    main()
