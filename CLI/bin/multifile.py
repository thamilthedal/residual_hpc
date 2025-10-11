from CLI.bin.cluster import fetch_report_file_path
from CLI.bin.monitor import FileMonitorPlot
from CLI.lib.plot_settings import color, contrast, mode, RES_STYLE
from CLI.bin.animate import animate_plot, init_plot


UPDATE_INTERVAL_SECONDS = 30
X = [0, 100, 10, "linear"]
Y = [0, 100, 10, "linear"]

def multi_file_monitor():

    [fig, axes, job_ids, case_names] = init_plot(X, Y)

    monitors = []
    for n, id in enumerate(job_ids):
        out_file_path = fetch_report_file_path(id)
        # print(out_file_path)
        if out_file_path != None:
            monitor = FileMonitorPlot(axes[n], case_names[n], out_file_path, 
                                      r"$\mathrm{T_{w,max} (K)}$")
            monitors.append(monitor)

    if len(monitors) == 1:
        fig.suptitle(rf"$\mathbf{{Monitoring\ {{{len(job_ids)}}}\ report\ file}}$", 
                     fontsize = RES_STYLE["title_size"], 
                     color=contrast[mode])
    else:
        fig.suptitle(rf"$\mathbf{{Monitoring\ {{{len(job_ids)}}}\ report\ files}}$", 
                     fontsize = RES_STYLE["title_size"], 
                     color=contrast[mode])

    animate_plot(fig, monitors)

