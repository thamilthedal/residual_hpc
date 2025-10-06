from matplotlib import pyplot as plt
from classfile import ResidueMonitorPlot
from matplotlib.animation import FuncAnimation
from plotter.plot_utils import multi_plot

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


# --- Configuration ---
CASE_IDS = [
    r'$\mathbf{Case\ Alpha\ Wing}$', 
    r'$\mathbf{Case\ Beta\ Nozzle}$', 
    r'$\mathbf{Case\ Gamma\ Heat\ Ex}$', 
    r'$\mathbf{Case\ Delta\ Turbine}$'
]
RESIDUAL_NAMES = [
    r'$\mathbf{continuity}$', 
    r'$\mathbf{x}$', 
    r'$\mathbf{y}$', 
    r'$\mathbf{k}$', 
    r'$\mathbf{omega}$',
    r'$\mathbf{energy}$' 
]
UPDATE_INTERVAL_SECONDS = 10

# --- Main Application ---
fig, axes = multi_plot(["", "", ""],
                       [0, 1000, 100, "linear"],
                       [-2, 2, 1, "log"],
                       4,
                       style = RES_STYLE)

# fig, axes = plt.subplots(2, 2, figsize=(15, 11))
# fig.suptitle("Live Fluent Monitor with a Single Legend", fontsize=16)

plot_monitors = []
for ax, case_id in zip(axes, CASE_IDS):
    monitor = ResidueMonitorPlot(ax, case_id, RESIDUAL_NAMES)
    plot_monitors.append(monitor)

# --- NEW: Create a single, shared legend for the entire figure ---
# Get the handles (lines) and labels from the first subplot
# Since all plots have the same lines, we only need to do this once.
handles, labels = plot_monitors[0].ax.get_legend_handles_labels()
# Place the legend at the top of the figure, arranged in 6 columns
fig.legend(handles, labels, loc='upper center', ncol=len(RESIDUAL_NAMES))

def update_all_plots(frame):
    for monitor in plot_monitors:
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
