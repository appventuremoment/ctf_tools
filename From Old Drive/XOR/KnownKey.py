import base64
from pwn import *
k1 = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

#print(bytes.fromhex("0x22"))
#print(bytes.fromhex(str(hex(2))))

temp = xor(k1, b"myXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkeymyXORkey")
print(temp)
