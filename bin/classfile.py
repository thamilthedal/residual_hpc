import matplotlib.pyplot as plt
import numpy as np
from lib.plot_settings import alpha, palettes, mode
from lib.helper import get_data, get_residue, extract_scale
from functools import cache


class ResidueMonitorPlot:
    """
    Manages a single subplot for live monitoring of multiple residual
    equations from an ANSYS Fluent case.
    """
    def __init__(self, ax, case_id, residual_names, file_path):
        self.ax = ax
        self.case_id = case_id
        self.residual_names = residual_names
        self.file_path = file_path
        self.lines = {}
        self.ax.set_title(rf"$\mathrm{{{self.case_id}}}$")
        # self.ax.set_xlabel(r"$\mathbf{N_{iterations}}$")
        # self.ax.set_ylabel(r"$\mathbf{Residuals}$")
        self.ax.grid(True, which="both", linestyle='--', alpha=alpha[mode])
        self.ax.set_xscale("log")
        self.ax.set_yscale("log")
        for i, name in enumerate(self.residual_names):
            line, = self.ax.plot([], [], label=name, color=palettes[mode][name], linestyle='--', alpha=0.8)
            self.lines[str(i+1)] = line

    @cache
    def update_plot(self):
        iterations, residuals_dict = get_residue(self.file_path)
        X, Y = extract_scale(iterations, residuals_dict)
        
        folder = self.file_path.split("/")[-2]
        # print(iterations)
        # print(X, Y)
        title = rf"$\mathrm{{{self.case_id}\ [{folder}]}}$"
        self.ax.set_title(title)
        self.ax.set_xlim(10**X[0], 10**X[1])
        self.ax.set_xscale(X[3])
        self.ax.set_ylim(Y[0], Y[1] + Y[2])
        self.ax.set_yscale(Y[3])
        
        if residuals_dict.index is not None and len(residuals_dict.index) > 0:
            for n, i in enumerate(residuals_dict.columns[1:-2]):
                self.lines[str(n+1)].set_data(iterations, residuals_dict[i])

class FileMonitorPlot:
    """
        Manages a single subplot for live monitoring of report files for ANSYS Fluent case
    """
    def __init__(self, ax, case_id, file_path, label):
        self.ax = ax
        self.case_id = case_id
        self.file_path = file_path
        self.label = label
        self.lines = {}
        self.ax.set_title(rf"$\mathrm{{{self.case_id}}}$")
        self.ax.set_xlabel(r"$\mathrm{N_{\Delta t}}$")
        self.ax.set_ylabel(self.label)
        self.ax.grid(True, which="both", linestyle='--', alpha=alpha[mode])

        line, = self.ax.plot([], [], color=palettes[mode]['k'],
                             linestyle='--')

        self.lines[case_id] = line

    def update_plot(self):

        [timestep, values] = get_data(self.file_path)
        # print(values)

        if timestep is not None and len(timestep) > 0:
            X = [min(timestep), max(timestep), (max(timestep) - min(timestep)) / 5, "linear"]
            Y = [min(values), max(values), (max(values) - min(values)) / 5, "linear"]

            folder = self.file_path.split("/")[-2]

            title = rf"$\mathrm{{{self.case_id}}}$" + " " + self.label + rf"$\mathrm{{\ at\ \Delta t\ of\ {timestep[-1]} = {values[-1]:.3f}\ [{folder}]}}$"
            self.ax.set_title(title)
            self.ax.set_xlim(X[0], X[1] + X[2])
            self.ax.set_xscale(X[3])
            self.ax.set_ylim(Y[0], Y[1] + Y[2])
            self.ax.set_yscale(Y[3])
            self.lines[self.case_id].set_data(timestep, values)
