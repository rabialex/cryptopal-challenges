from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from helper import load_file

import base64
import pprint

def AES(msg, key):

        
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()

    return encryptor.update(msg) + encryptor.finalize()

def AES_decryptor(ciphertext, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()

    return decryptor.update(ciphertext) + decryptor.finalize()

if __name__ == "__main__":
    
    key = b"YELLOW SUBMARINE"
    ciphertext = "".join(load_file("ch7.txt"))
    ciphertext = base64.b64decode(ciphertext)
    msg = AES_decryptor(ciphertext, key).decode()

    print(msg.rstrip())