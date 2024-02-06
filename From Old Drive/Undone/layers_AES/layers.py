from Crypto.Cipher import AES
import os

key1 = os.urandom(16)
key2 = os.urandom(16)
iv = os.urandom(16)

def ofb(data):
    cipher = AES.new(key1, AES.MODE_OFB, iv=iv)
    return cipher.encrypt(data)

def ctr(data):
    cipher = AES.new(key2, AES.MODE_CTR, nonce=iv[:8])
    return cipher.encrypt(data)

flag = b"???"
b = ofb(flag)
c = ctr(b)
d = ctr(flag)

print(f"{b = }")
print(f"{c = }")
print(f"{d = }")

#This was also given
'''
b = b'\xa0j\x9e\xca\xf3R\xfc\x90:b\x93i\xf7\xa9\x00\xea\x8dp\x00\xd1\x08'
c = b'X\xf38U;%\xb7|1\xae\xfc!\xbe\x81zmg\xe1\xec\xb9S'
d = b'\x9e\xf5\xc7\xf8\xb3\x04.\x8f~\xbe\n\x171G\x08\xd8\x84\xfe\x98W&'
'''
