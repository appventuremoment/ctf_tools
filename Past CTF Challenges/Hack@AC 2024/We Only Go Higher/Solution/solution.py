from pwn import *
from Crypto.Util.number import *

maxnum = 0
multi = 1
for i in range(80):
    maxnum += 9 * multi * 2
    multi *= 22

maxguess = int('9' * 80)
minguess = 0

p = remote("beta.hackac.live", 3002)
target = int(p.recv().decode().split(' ')[3][:-5])


encguess = 0
guess = (minguess + maxguess) // 2
while encguess != target:
    try:
        p.sendline(bytes(str(guess), 'utf-8'))
        encguess = int(p.recv().decode().split(' ')[2][3:-8])
        if encguess > target:
            maxguess = guess
        elif encguess < target:
            minguess = guess
        guess = (minguess + maxguess) // 2
        print(guess)
    except:
        break

print(long_to_bytes(guess).decode())