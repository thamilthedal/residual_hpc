import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rcParams as rc

def set_plot(Title, X, Y, size, style):
    # Changing Font of Plot
    if style is None:
        style = default_style
    rc['mathtext.fontset'] = 'cm'
    rc['font.family'] = 'sans-serif'
    rc['font.sans-serif'] = [style["font"]]
    rc['axes.linewidth'] = style["line_width"]
    rc['lines.linewidth'] = style["line_width"]
    rc['lines.markerfacecolor'] = 'w'
    rc['lines.markersize'] = 5
    rc['legend.fontsize'] = style["internal_fontsize"]

    fig = plt.figure(figsize=size, tight_layout=True)
    a = fig.add_subplot(111)

    # Titles
    a.set_title(Title[0], fontsize=style["title_size"], fontweight=style["label_weight"])
    a.set_xlabel(Title[1], fontsize=style["label_size"], fontweight=style["label_weight"])
    a.set_ylabel(Title[2], fontsize=style["label_size"], fontweight=style["label_weight"])

    # Axis Limits Grid and Ticks

    # Set Axis Limits
    a.axis([X[0], X[1], Y[0], Y[1]])

    # Set Plot Border
    a.spines['right'].set_visible(style["border"][0])
    a.spines['top'].set_visible(style["border"][1])
    a.spines['left'].set_visible(style["border"][2])
    a.spines['bottom'].set_visible(style["border"][3])

    # Grid ON/OFF
    # a.grid('off',color='k',linestyle='dashed',alpha=0.5)

    # Global Tick Parameters
    a.tick_params(direction='out', length=5, width=1, colors='k', labelsize = style["internal_fontsize"])
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


def multi_plot(Title, X, Y, n_plots, style):

    rc['mathtext.fontset'] = 'cm'
    rc['font.family'] = 'sans-serif'
    rc['font.sans-serif'] = [style["font"]]
    rc['axes.linewidth'] = style["line_width"]
    rc['lines.linewidth'] = style["line_width"]
    rc['lines.markerfacecolor'] = 'w'
    rc['lines.markersize'] = style["marker_size"]
    rc['legend.fontsize'] = style["internal_fontsize"]

    if n_plots == 4:
        plot_info = 221
    if n_plots == 6:
        plot_info = 231
    if n_plots == 9:
        plot_info = 331
    
    fig = plt.figure(figsize=(17,9), tight_layout=True)
    plots = []
    for i in range(n_plots):
        plots.append(fig.add_subplot(plot_info+i))



    for a in plots:
        a.set_title(Title[0], 
                    fontsize=style["title_size"], 
                    fontweight=style["label_weight"])
        a.set_xlabel(Title[1], 
                     fontsize=style["label_size"], 
                     fontweight=style["label_weight"])
        a.set_ylabel(Title[2], 
                     fontsize=style["label_size"], 
                     fontweight=style["label_weight"])

        # Axis Limits Grid and Ticks

        # Set Axis Limit Offsets
        x_offset = 0 if len(X) == 4 else X[4]
        y_offset = 0 if len(Y) == 4 else Y[4]

        
        # Set Axis Limits
        if X[3] != "log" and Y[3] != "log":
            print("linear plot")
            a.axis([X[0]-x_offset, X[1]+x_offset, Y[0]-y_offset, Y[1]+y_offset])

        # Set Plot Border
        a.spines['right'].set_visible(style["border"][0])
        a.spines['top'].set_visible(style["border"][1])
        a.spines['left'].set_visible(style["border"][2])
        a.spines['bottom'].set_visible(style["border"][3])

        # Grid ON/OFF
        # a.grid(style['grid'],color='k',linestyle='dashed',alpha=0.5)

        # Global Tick Parameters
        a.tick_params(direction='out', 
                      length=5, 
                      width=style["tick_width"], 
                      colors='k', 
                      labelsize = style["internal_fontsize"])
        for label in a.get_xticklabels():
            label.set_fontweight('bold')
        for label in a.get_yticklabels():
            label.set_fontweight('bold')
        
        # X tick Parameters
        if X[3] == 'linear':
            xticks = np.arange(X[0], X[1] + X[2], X[2])
            # print(xticks)
            a.set_xticks(xticks)
        else:
            a.set_xscale(X[3])
            xticks = 10.0**np.arange(X[0], X[1], X[2])
            # print(xticks)
            a.set_xticks(xticks)
        
        # Y tick Parameters
        if Y[3] == 'linear':
            yticks = np.arange(Y[0], Y[1] + Y[2], Y[2])
            # print(yticks)
            a.set_yticks(yticks)
        else:
            a.set_yscale(Y[3])
            yticks = 10.0**np.arange(Y[0], Y[1], Y[2])
            # print(yticks)
            a.set_yticks(yticks)

    return [fig, plots]

