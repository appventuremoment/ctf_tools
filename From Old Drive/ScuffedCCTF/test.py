from Crypto.Util.number import *
from pwn import *
for i in range(30):
    conn = remote('mango.local', i)
    conn.recvline() 
    conn.close