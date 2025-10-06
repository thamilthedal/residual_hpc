from CLI.bin.cluster import get_jobs, fetch_out_file_path
from CLI.bin.monitor import ResidueMonitorPlot
from CLI.lib.plot_utils import multi_plot
from CLI.lib.plot_settings import color, contrast, mode, RES_STYLE
from CLI.bin.animate import animate_plot


residual_names = ["continuity", "x-velocity", "y-velocity", "energy", "k", "omega"]
Title = ["", "", ""]
X = [0, 100, 10, "linear"]
Y = [-2, 2, 1, "log"]


def multi_residue_monitor():

    final_cases = get_jobs()

    if len(final_cases) > 0:
        case_names = final_cases["JOB_NAME"].to_list()
        job_ids = final_cases["JOB_ID"].to_list()
    else:
        raise ValueError

    fig, axes = multi_plot(X, Y, len(job_ids))

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
