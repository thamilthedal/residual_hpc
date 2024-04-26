import sys
from lib.plot_utils import set_plot
from lib.plot_settings import PLOT_STYLE_RES, RES_MARKERS

# SSH Credentials
HOST_NAME = 'xyz.com'
USER = 'userid'
PWD = '********'

# Plot Details
file_name = sys.argv[1].split('/')[-1].split('.')[0]
Title = [f"${file_name}$", "$Number\ of\ Iterations$", "$Normalized\ Residuals$"]
X = [0, 1, 0.1, "linear"]
Y = [0.1, 1000, 10, "log"]

fig, ax = set_plot(Title, X, Y, (8, 6), style=PLOT_STYLE_RES)

WORDS = ['flow', '#', 'warning', 'details', 'Time', 'survey.', 'anonymous', 'use']
