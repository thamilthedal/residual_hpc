from typing import Dict, List
import pandas as pd
import os
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rcParams

DEFAULT_STYLE: dict[str, list[bool] | int | str | float] = {
    "font": 'Arial',
    "title_size": 20,
    "label_size": 16,
    "internal_fontsize":16,
    "label_weight": 'bold',
    "line_width": 1.5,
    "border": [True, True, True, True],
}

RES_MARKERS = [
        'k--',
        'r-.',
        'g:',
        'b--',
        'm-',
        'c:',
        '-'
        ]


def set_plot(Title, X, Y, size=(8, 6.5), style=DEFAULT_STYLE, subplots=111):
    # Changing Font of Plot
    rcParams['axes.linewidth'] = style["line_width"]
    rcParams['lines.linewidth'] = style["line_width"]
    rcParams['lines.markerfacecolor'] = 'w'
    rcParams['lines.markersize'] = 5
    rcParams['legend.fontsize'] = style["internal_fontsize"]

    fig = plt.figure(figsize=size, tight_layout=True)
    a = fig.add_subplot(subplots)

    # Titles
    a.set_title(Title[0], fontsize=style["title_size"], fontweight=style["label_weight"])
    a.set_xlabel(Title[1], fontsize=style["label_size"], fontweight=style["label_weight"])
    a.set_ylabel(Title[2], fontsize=style["label_size"], fontweight=style["label_weight"])

    # Axis Limits Grid and Ticks

    # Set Axis Limits
    x_offset = 0 if len(X) == 4 else X[4]
    y_offset = 0 if len(Y) == 4 else Y[4]

    a.axis([X[0]-x_offset, X[1]+x_offset, Y[0]-y_offset, Y[1]+y_offset])

    # Set Plot Border
    a.spines['right'].set_visible(style["border"][0])
    a.spines['top'].set_visible(style["border"][1])
    a.spines['left'].set_visible(style["border"][2])
    a.spines['bottom'].set_visible(style["border"][3])

    # Grid ON/OFF
    # a.grid('off',color='k',linestyle='dashed',alpha=0.5)

    # Global Tick Parameters
    a.tick_params(direction='out', length=5, width=1, colors='k',
                  labelsize=style["internal_fontsize"])
    # X tick Parameters
    if X[3] == 'linear':
        a.set_xticks(np.arange(X[0], X[1] + X[2], X[2]))
    else:
        a.set_xscale(X[3])
    # Y tick Parameters
    if Y[3] == 'linear':
        a.set_yticks(np.arange(Y[0], Y[1] + Y[2], Y[2]))
    else:
        a.set_yscale(Y[3])

    return [fig, a]


