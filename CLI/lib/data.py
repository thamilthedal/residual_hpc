import sys
import os 
from dotenv import load_dotenv

# from lib.plotter import set_plot, plt, RES_MARKERS

dotenv_path = './.env'
load_dotenv(dotenv_path)

HOST_NAME = str(os.environ.get("HOST_NAME"))
USER = str(os.environ.get("UNAME"))
PWD = str(os.environ.get("PASS"))
CONV_CRITERIA = float(os.environ.get("CONV_CRITERIA"))

# Plot Details
# Title = ["", "Number of Iterations", "Normalized Residuals"]
# X = [0, 1, 0.1, "linear"]
# Y = [0.1, 1000, 10, "log"]

# fig, ax = set_plot(Title, X, Y, (8, 6))

WORDS = ['flow', '#', 'warning', 'details', 'Time', 'survey.', 'anonymous', 'use', 'Solution', 'UDS', 'continuity', 'Clock']
