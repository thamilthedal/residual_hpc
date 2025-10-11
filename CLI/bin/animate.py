from CLI.bin.cluster import get_jobs
from matplotlib import pyplot as plt
from CLI.lib.plot_utils import multi_plot
from matplotlib.animation import FuncAnimation
from CLI.data import UPDATE_INTERVAL_SECONDS


def animate_plot(fig, monitors):

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

    # Adjust layout to make space for the new legend and the main title
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    if len(monitors) > 1:
        plt.get_current_fig_manager().window.state('zoomed')
    else:
        plt.get_current_fig_manager().window.geometry('1300x900+0+0')
    plt.show()


def init_plot(X, Y):

    final_cases = get_jobs()

    if len(final_cases) > 0:
        case_names = final_cases["JOB_NAME"].to_list()
        job_ids = final_cases["JOB_ID"].to_list()
    else:
        raise ValueError

    fig, axes = multi_plot(X, Y, len(job_ids))

    return [fig, axes, job_ids, case_names]
