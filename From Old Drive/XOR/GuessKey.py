from pwn import *


message =  bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

partial_key = xor(message[:7], "crypto{").decode() + 'y'
complete_key = (partial_key * (len(message)//len(partial_key) + 1))[:len(message)]
print(complete_key)
flag = xor(message, complete_key)

print(flag)
