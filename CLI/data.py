import os
from CLI.first_login import first_login
from dotenv import load_dotenv
from cryptography.fernet import Fernet

def decrypt_data(key_str, cipher_text_str):
    """Decrypt using Fernet key and ciphertext (both as strings)"""
    key = key_str.strip().encode()
    cipher_text = cipher_text_str.strip().encode()
    fernet = Fernet(key)
    plain_text = fernet.decrypt(cipher_text)
    return plain_text.decode('utf-8')

dotenv_path = './.env'

# Run first_login if .env does not exist
if not os.path.exists(dotenv_path):
    first_login()

load_dotenv(dotenv_path)

# Fetch and decrypt credentials
HOST_K = os.getenv("HOST_K")
HOST_C = os.getenv("HOST_C")
USER_K = os.getenv("USER_K")
USER_C = os.getenv("USER_C")
PASS_K = os.getenv("PASS_K")
PASS_C = os.getenv("PASS_C")

if HOST_K and HOST_C:
    HOST_NAME = decrypt_data(HOST_K, HOST_C)
else:
    HOST_NAME = None

if USER_K and USER_C:
    USER = decrypt_data(USER_K, USER_C)
else:
    USER = None

if PASS_K and PASS_C:
    PWD = decrypt_data(PASS_K, PASS_C)
else:
    PWD = None


# import sys
# import os 
# from dotenv import load_dotenv

# # from lib.plotter import set_plot, plt, RES_MARKERS

# dotenv_path = './.env'
# load_dotenv(dotenv_path)

# HOST_NAME = str(os.environ.get("HOST_NAME"))
# USER = str(os.environ.get("UNAME"))
# PWD = str(os.environ.get("PASS"))
# # <<<<<<< HEAD
# # CONV_CRITERIA = float(os.environ.get("CONV_CRITERIA"))
UPDATE_INTERVAL_SECONDS = 15
SAMPLING_DATA = 5000
# # =======
# # # CONV_CRITERIA = float(os.environ.get("CONV_CRITERIA"))
# # UPDATE_INTERVAL_SECONDS = 30
# # SAMPLING_DATA = 10000
# # >>>>>>> 364c268b32cf8df9a36a86eb212a28d7bec00c4e

# # Plot Details
# # Title = ["", "Number of Iterations", "Normalized Residuals"]
# # X = [0, 1, 0.1, "linear"]
# # Y = [0.1, 1000, 10, "log"]

# # fig, ax = set_plot(Title, X, Y, (8, 6))

# WORDS = ['flow', '#', 'warning', 'details', 'Time', 'survey.', 'anonymous', 'use', 'Solution', 'UDS', 'continuity', 'Clock']
