from CLI.bin.cluster import get_jobs, fetch_report_file_path
from CLI.bin.monitor import FileMonitorPlot
from CLI.lib.plot_utils import multi_plot
from CLI.lib.plot_settings import color, contrast, mode, RES_STYLE
from CLI.bin.animate import animate_plot


UPDATE_INTERVAL_SECONDS = 30
X = [0, 100, 10, "linear"]
Y = [0, 100, 10, "linear"]

def multi_file_monitor():

    final_cases = get_jobs()

    if len(final_cases) > 0:
        case_names = final_cases["JOB_NAME"].to_list()
        job_ids = final_cases["JOB_ID"].to_list()
    else:
        raise ValueError

    fig, axes = multi_plot(X, Y, len(job_ids))

    monitors = []
    for n, id in enumerate(job_ids):
        out_file_path = fetch_report_file_path(id)
        # print(out_file_path)
        monitor = FileMonitorPlot(axes[n], case_names[n], out_file_path, 
                                  r"$\mathrm{T_{w,max} (K)}$")
        monitors.append(monitor)

    fig.suptitle(rf"$\mathbf{{Monitoring\ {{{len(job_ids)}}}\ report\ files}}$", 
                 fontsize = RES_STYLE["title_size"], 
                 color=contrast[mode])

    animate_plot(fig, monitors)

