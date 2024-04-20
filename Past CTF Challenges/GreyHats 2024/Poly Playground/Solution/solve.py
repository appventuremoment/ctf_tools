from pwn import *
from numpy.polynomial import polynomial as P

r = connect('challs.nusgreyhats.org', 31113)


temp = b"Present the coefficients of your amazing equation:"

while True:
    temp = r.recv()
    if b"Present the coefficients of your amazing equation:" not in temp:
        break
    # print(temp.decode())
    roots = temp.decode().split('Roots: ')[1].split('\n')[0].split(',')
    roots = list(map(int, roots))
    
    answer = list(map(int, list(P.polyfromroots(roots))))[::-1]
    # print(answer)
    ret = ""
    for i in answer:
        ret += str(i) + ", "

    ret = ret[:-2].encode()
    r.sendline(ret)

print(temp.decode())
r.close()