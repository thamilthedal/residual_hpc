from CLI.bin.cluster import fetch_out_file_path
from CLI.bin.monitor import ResidueMonitorPlot
from CLI.lib.plot_settings import color, contrast, mode, RES_STYLE
from CLI.bin.animate import animate_plot, init_plot


residual_names = ["continuity", "x-velocity", "y-velocity", "energy", "k", "omega"]
Title = ["", "", ""]
X = [-3, 3, 1, "log"]
Y = [-2, 2, 1, "log"]


def multi_residue_monitor():

    [fig, axes, job_ids, case_names] = init_plot(X, Y)

    monitors = []
    for n, id in enumerate(job_ids):
        out_file_path = fetch_out_file_path(id)
        # print(out_file_path)
        monitor = ResidueMonitorPlot(axes[n], case_names[n], residual_names, 
                                     out_file_path)
        monitors.append(monitor)

    handles, labels = monitors[0].ax.get_legend_handles_labels()
    fig.supxlabel(r"$\mathbf{N_{iterations}}$", fontsize=RES_STYLE["label_size"])
    fig.supylabel(r"$\mathbf{Residuals}$", fontsize=RES_STYLE["label_size"])
    fig.legend(handles, labels, 
               loc='upper center', 
               ncol=len(residual_names), 
               fontsize=RES_STYLE["internal_fontsize"])

    animate_plot(fig, monitors)
