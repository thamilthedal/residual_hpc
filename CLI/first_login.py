from cryptography.fernet import Fernet

def encrypt_data(data: str):
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(data.encode('utf-8'))
    return key, cipher_text

def store_data(key1, key2, cipher_text1, cipher_text2):
    
    with open("./.env", "a") as f:
        f.write(f"{key1}={cipher_text1.decode()}\n")
        f.write(f"{key2}={cipher_text2.decode()}\n")


def first_login():
    input_host = input("Enter the Hostname: ")
    input_user = input("Enter the Username: ")
    input_pass = input("Enter the Password: ")

    HOST_K, HOST_C = encrypt_data(input_host)
    store_data("HOST_K", "HOST_C", HOST_K, HOST_C)
    USER_K, USER_C = encrypt_data(input_user)
    store_data("USER_K", "USER_C", USER_K, USER_C)
    PASS_K, PASS_C = encrypt_data(input_pass)
    store_data("PASS_K", "PASS_C", PASS_K, PASS_C)
