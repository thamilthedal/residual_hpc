from matplotlib import pyplot as plt
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
    plt.get_current_fig_manager().window.state('zoomed')
    plt.show()
