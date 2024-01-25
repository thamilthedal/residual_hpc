from lib.plot_utils import set_plot, plt
import monitor.data as md
from monitor.helper import convert_float, extract_scale

def monitor_residue(file_name, residue, residue_label):
    residue = convert_float(residue)
    [X, Y] = extract_scale(residue)
    file = file_name.split('/')[-1].split('.')[0]
    md.TITLE[0] = file
    [fig, window] = set_plot(md.TITLE, X, Y, (15, 8))

    for i in residue.columns:
        window.plot(residue.index, 
                    residue.iloc[:, i],
                    '--',
                    label = residue_label[i])
    window.legend()
    fig.show()
    plt.pause(60)
    plt.clf()
    plt.close()
