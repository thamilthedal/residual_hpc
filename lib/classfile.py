import matplotlib.pyplot as plt
import numpy as np
# from src.fetch_data import fetch_latest_residue_data
# from plotter.plot_settings import MARKERS
from lib.helper import get_data

# from src.multi_animate import case_id


# class ResidueMonitorPlot:
#     """
#     Manages a single subplot for live monitoring of multiple residual
#     equations from an ANSYS Fluent case.
#     """
#     def __init__(self, ax, case_id, residual_names):
#         self.ax = ax
#         self.case_id = case_id
#         self.residual_names = residual_names
#         self.lines = {}
#
#         self.ax.set_title(self.case_id)
#         self.ax.set_xlabel(r"$\mathbf{N_{iterations}}$")
#         self.ax.set_ylabel(r"$\mathbf{Residuals}$")
#         self.ax.grid(True, which="both", linestyle='--', alpha=0.5)
#         # self.ax.set_yscale('log')
#
#         # Create a line artist for each residual equation, including its label
#         for i, name in enumerate(self.residual_names):
#             line, = self.ax.plot([], [], label=name, color=MARKERS['colors'][i],
#                                  marker=MARKERS['markers'][i], linestyle=MARKERS['linestyles'][i], alpha=0.8)
#             self.lines[name] = line
#
#         # REMOVED: self.ax.legend() is no longer called here.
#
#     def update_plot(self):
#         iterations, residuals_dict = fetch_latest_residue_data(self.case_id, self.residual_names)
#
#         if iterations is not None and len(iterations) > 0:
#             for name, values in residuals_dict.items():
#                 if name in self.lines:
#                     self.lines[name].set_data(iterations, values)
#
#             # self.ax.set_xlim(X[0], X[1]+X[2])
#             # self.ax.set_xscale(X[3])
#             # self.ax.set_ylim(Y[0], Y[1]+Y[2])
#             # self.ax.set_yscale(Y[3])
#             self.ax.relim()
#             self.ax.autoscale_view()

class FileMonitorPlot:
    """
        Manages a single subplot for live monitoring of report files for ANSYS Fluent case
    """
    def __init__(self, fig, ax, case_id, file_path, label):
        self.fig = fig
        self.ax = ax
        self.case_id = case_id
        self.file_path = file_path
        self.label = label
        self.lines = {}
        self.ax.set_title(rf"$\mathrm{{{self.case_id}}}$")
        self.ax.set_xlabel(r"$\mathrm{N_{\Delta t}}$")
        self.ax.set_ylabel(self.label)
        self.ax.grid(True, which="both", linestyle='--', alpha=0.5)

        line, = self.ax.plot([], [], color='r',
                             linestyle='--', alpha=0.8)

        self.lines[case_id] = line

    def update_plot(self):

        [timestep, values] = get_data(self.file_path)
        # print(values)

        if timestep is not None and len(timestep) > 0:
            X = [min(timestep), max(timestep), (max(timestep) - min(timestep)) / 5, "linear"]
            Y = [min(values), max(values), (max(values) - min(values)) / 5, "linear"]

            title = rf"$\mathrm{{{self.case_id}}}$" + " " + self.label + f" = {values[-1]:.3f}"
            self.ax.set_title(title)
            self.ax.set_xlim(X[0], X[1] + X[2])
            self.ax.set_xscale(X[3])
            self.ax.set_ylim(Y[0], Y[1] + Y[2])
            self.ax.set_yscale(Y[3])
            self.lines[self.case_id].set_data(timestep, values)
