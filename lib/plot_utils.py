from matplotlib import pyplot as plt
from matplotlib import rcParams as rc

def set_plot(Title, X, Y, size=(8,6.5)):

    #Changing Font of Plot
    rc['mathtext.fontset'] = 'cm'
    rc['font.family'] = 'sans-serif'
    rc['font.sans-serif'] = ['Times New Roman']
    rc['axes.linewidth'] = 1.2

    fig=plt.figure(figsize=size,tight_layout=True)
    a = fig.add_subplot(111)

    #Titles
    a.set_title(Title[0],fontsize=18,fontweight='bold')
    a.set_xlabel(Title[1],fontsize = 14,fontweight='bold')
    a.set_ylabel(Title[2],fontsize = 14,fontweight='bold')

    #Axis Limits Grid and Ticks

    # Set Axis Limits
    a.axis([X[0],X[1],Y[0],Y[1]])

    # Set Plot Border
    a.spines['right'].set_visible(False)
    a.spines['top'].set_visible(False)
    a.spines['left'].set_visible(True)
    a.spines['bottom'].set_visible(True)

    # Grid ON/OFF
    #a.grid('off',color='k',linestyle='dashed',alpha=0.5)
    # Global Tick Parameters
    a.tick_params(direction='out', length=5, width=1, colors='k')
    # X tick Parameters
    if X[3]=='linear':
        a.set_xticks(np.arange(X[0],X[1]+X[2],X[2]))
    else:
        a.set_xscale(X[3])

    # Y tick Parameters
    if Y[3]=='linear':
        a.set_yticks(np.arange(Y[0],Y[1]+Y[2],Y[2]))
    else:
        a.set_yscale(Y[3])

    return [fig, a]
