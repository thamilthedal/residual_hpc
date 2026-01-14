import matplotlib.pyplot as plt
import numpy as np
from CLI.lib.plot_settings import alpha, palettes, mode
from CLI.lib.helper import get_data, get_residue, extract_scale, calculate_eta


class BaseMonitorPlot:
    """
    Base Class for Monitor Plots
    """

    def __init__(self, ax, case_id, file_path, start_time):
        self.ax = ax
        self.case_id = case_id
        self.file_path = file_path
        self.folder = self.file_path.split("/")[-2]
        self.start = start_time


class ResidueMonitorPlot(BaseMonitorPlot):
    """
    Manages a single subplot for live monitoring of multiple residual
    equations from an ANSYS Fluent case.
    """
    def __init__(self, ax, case_id, residual_names, file_path, start_time):
        super().__init__(ax, case_id, file_path, start_time)
        self.residual_names = residual_names
        self.lines = {}
        self.ax.set_title(rf"$\mathrm{{{self.case_id}}}$")
        self.ax.grid(True, which="both", linestyle='--', alpha=alpha[mode])
        # self.ax.set_xscale("log")
        # self.ax.set_yscale("log")
        for i, name in enumerate(self.residual_names):
            line, = self.ax.plot([], [], label=fr"$\mathbf{{{name}}}$", color=palettes[mode][name], alpha=0.8)
            self.lines[str(i+1)] = line

    def update_plot(self):
        residuals_dict = get_residue(self.file_path)
        X, Y = extract_scale(residuals_dict)
        # print(iterations)
        # print(X, Y)
        elapsed = calculate_eta(self.start)
        title = rf"$\mathrm{{{self.case_id}\ [{self.folder}]\ Elapsed: {elapsed}\ h}}$"
        self.ax.set_title(title)
        self.ax.set_xlim(X[0], X[1])


        # x_ticks = np.logspace(np.log10(X[0]), np.log10(X[1]), 5, endpoint=True)
        # self.ax.set_xticks(x_ticks)
        self.ax.set_xscale(X[3])
        self.ax.set_ylim(Y[0], Y[1] + Y[2])
        self.ax.set_yscale(Y[3])
        for label in self.ax.get_xticklabels(which="both"):
            label.set_fontweight('bold')
        
        if residuals_dict.index is not None and len(residuals_dict.index) > 0:
            for n, i in enumerate(residuals_dict.columns[1:]):
                self.lines[str(n+1)].set_data(residuals_dict["iter"], residuals_dict[i])

class FileMonitorPlot(BaseMonitorPlot):
    """
        Manages a single subplot for live monitoring of report files for ANSYS Fluent case
    """
    def __init__(self, ax, case_id, file_path, label, start_time):
        super().__init__(ax, case_id, file_path, start_time)
        self.label = label
        self.lines = {}
        self.ax.set_title(rf"$\mathrm{{{self.case_id}}}$")
        self.ax.set_xlabel(r"$\mathrm{N_{\Delta t}}$")
        self.ax.set_ylabel(self.label)
        self.ax.grid(True, which="both", linestyle='--', alpha=alpha[mode])

        line, = self.ax.plot([], [], color=palettes[mode]['k'])

        self.lines[case_id] = line

    def update_plot(self):

        [timestep, values] = get_data(self.file_path)
        # print(values)

        if timestep is not None and len(timestep) > 0:
            X = [min(timestep), max(timestep), (max(timestep) - min(timestep)) / 4, "linear"]
            Y = [min(values), max(values), (max(values) - min(values)) / 4, "linear"]

            Twavg = np.mean(values[:-100])

            title = rf"$\mathrm{{{self.case_id}}}$ " + rf"$\mathrm{{\ At\ \Delta t\ ({int(timestep[-1])}),\ T_{{w,avg,100}} = {Twavg:.2f}\ K\ [{self.folder}]}}$"
            self.ax.set_title(title)
            self.ax.set_xlim(X[0], X[1] + X[2])
            self.ax.set_xscale(X[3])
            self.ax.set_ylim(Y[0], Y[1] + Y[2])
            self.ax.set_yscale(Y[3])
            self.lines[self.case_id].set_data(timestep, values)
