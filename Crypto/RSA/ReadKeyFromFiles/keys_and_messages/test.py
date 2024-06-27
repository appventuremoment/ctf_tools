from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.number import *

Nis = []
for filename in range(1, 51):
    with open(str(filename) + ".pem",'r') as file:
        out = RSA.importKey(file.read())
        Nis.append(out.n)

sharedPrimes = []
for x in Nis:
    for y in Nis:
        if x != y and GCD(x, y) != 1:
            sharedPrimes.append(GCD(x,y))

with open('21.pem') as f:
    key = RSA.importKey(f.read())
    n = key.n
    e = key.e

print(len(sharedPrimes))
for p in sharedPrimes:
    if n % p == 0:
        q = n // p
        print(q)
        d = pow(e, -1, (p - 1) * (q - 1))
        key = RSA.construct((n, e, d))
        break


with open('21.ciphertext', 'r') as f:
    msg = int(f.read(), 16)
    msg = long_to_bytes(msg)
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.decrypt(msg)
    print(ciphertext)