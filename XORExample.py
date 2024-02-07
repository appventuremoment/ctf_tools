import base64
from pwn import *
k1 = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
print(xor(k1, b'crypto{'))

#find key is "myXORke......"
#infer it is "myXORkey" repeated

temp = xor(k1, b"myXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkey")
print(temp)
