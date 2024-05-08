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
