import os
from dotenv import load_dotenv
from cryptography.fernet import Fernet


def encrypt_data(data: str):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(data.encode('utf-8'))
    return key, cipher_text


def decrypt_data(key_str, cipher_text_str):
    """Decrypt using Fernet key and ciphertext (both as strings)"""
    key = key_str.strip().encode()
    cipher_text = cipher_text_str.strip().encode()
    fernet = Fernet(key)
    plain_text = fernet.decrypt(cipher_text)
    return plain_text.decode('utf-8')


def store_data(key1, key2, cipher_text1, cipher_text2):
    with open("./.env", "a") as f:
        f.write(f"{key1}={cipher_text1.decode()}\n")
        f.write(f"{key2}={cipher_text2.decode()}\n")


def first_login():
    input_host = input("Enter the IP Address: ")
    input_user = input("Enter the Username: ")
    input_pass = input("Enter the Password: ")

    HOST_K, HOST_C = encrypt_data(input_host)
    store_data("HOST_K", "HOST_C", HOST_K, HOST_C)
    USER_K, USER_C = encrypt_data(input_user)
    store_data("USER_K", "USER_C", USER_K, USER_C)
    PASS_K, PASS_C = encrypt_data(input_pass)
    store_data("PASS_K", "PASS_C", PASS_K, PASS_C)


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