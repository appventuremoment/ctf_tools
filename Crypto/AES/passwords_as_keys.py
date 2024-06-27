from Crypto.Cipher import AES
from Crypto.Util.number import *
import hashlib
import random


print(hashlib.md5('TtttTT'.encode()).digest())

def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = hashlib.md5(password_hash.encode('utf-8')).digest()

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return "Error " + str(e)

    return decrypted.hex()

with open("password_list.txt", "r") as f:
    passwords = f.read().split('\n')

for i in passwords:
	temp = int(decrypt("c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66", i), 16)
	temp = long_to_bytes(temp)
	if b"crypto{" in temp:
		print(temp.decode())
		print(i)
