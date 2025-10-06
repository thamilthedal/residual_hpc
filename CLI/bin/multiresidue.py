from CLI.bin.cluster import get_jobs, fetch_out_file_path
from CLI.bin.classfile import ResidueMonitorPlot
from CLI.lib.plot_utils import multi_plot, plt
from CLI.lib.plot_settings import color, contrast, mode

from matplotlib.animation import FuncAnimation

RES_STYLE: dict[str, list[bool] | int | str | float] = {
    "font": 'Times New Roman',
    "title_size": 18,
    "label_size": 18,
    "internal_fontsize": 14,
    "label_weight": 'bold',
    "line_width": 1.8,
    "tick_width": 1.8,
    "border": [True, True, True, True],
    "grid": "off",
    "marker_size": 4
}

residual_names = ["continuity", "x", "y", "energy", "k", "omega"]


UPDATE_INTERVAL_SECONDS = 30

def multi_residue_monitor():

    final_cases = get_jobs()

    if len(final_cases) > 0:
        case_names = final_cases["JOB_NAME"].to_list()
        job_ids = final_cases["JOB_ID"].to_list()

    if len(job_ids) < 3:
        raise ValueError

    fig, axes = multi_plot(["", "", ""],
                           [1, 6, 2, "log"],
                           [-3, 3, 1, "log"],
                           len(job_ids),
                           style = RES_STYLE)

    monitors = []
    for n, id in enumerate(job_ids):
        out_file_path = fetch_out_file_path(id)
        # print(out_file_path)
        monitor = ResidueMonitorPlot(axes[n], case_names[n], residual_names, out_file_path)
        monitors.append(monitor)

    handles, labels = monitors[0].ax.get_legend_handles_labels()
    fig.supxlabel(r"$\mathbf{N_{iterations}}$", fontsize=RES_STYLE["label_size"])
    fig.supylabel(r"$\mathbf{Residuals}$", fontsize=RES_STYLE["label_size"])
    fig.legend(handles, labels, loc='upper center', ncol=len(residual_names), fontsize=RES_STYLE["internal_fontsize"])

    def update_all_plots(frame):
        for monitor in monitors:
            monitor.update_plot()

    ani = FuncAnimation(
        fig,
        update_all_plots,
        interval=UPDATE_INTERVAL_SECONDS * 1000,
        blit=False,
        cache_frame_data=False
    )

    # plt.close()
    # Adjust layout to make space for the new legend and the main title
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.get_current_fig_manager().window.state('zoomed')
    plt.show()
