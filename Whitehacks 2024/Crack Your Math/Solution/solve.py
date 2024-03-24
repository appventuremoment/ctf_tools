# Crack Your Math[**]
# Literally just math questions with addition and subtraction

from pwn import *

r = connect('ctf2.whitehats.site', 4001)

line = r.recv()

for i in range(123):    
    line = r.recv().decode().split(' ')[3:-1]
    line = " ".join(line).split("\n")[1]
    print(line)
    r.sendline(str(eval(line)).encode())
    print(r.recv())

print(r.recv())
print(r.recv())
print(r.recv())


r.close()