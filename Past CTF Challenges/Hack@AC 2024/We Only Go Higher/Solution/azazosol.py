from pwn import *
from operator import mul
from functools import reduce

def product(l):
    return reduce(mul, l, 1)

p = remote("beta.hackac.live", 3002)
p.recvuntil(b"Encrypted Secret:  ")
secret = int(p.recvline().strip().decode())

numbers1 = []
numbers2 = []

for i in range(80):
    p.recvuntil(b"Enter a positive base 10 number to encrypt: ")
    p.sendline(str(10**i).encode())
    p.recvline()
    number = int(p.recvline().strip().decode())
    if i == 0:
        numbers1.append(number)
        numbers2.append(1)
    else:
        gr = round(number/product(numbers2))
        if 19 <= gr <= 22:
            numbers1.append(1)
            numbers2.append(gr)
        else:
            numbers1.append(2)
            numbers2.append(gr//2)

print(len(numbers1), len(numbers2))
print(numbers1, numbers2)

from z3 import *
from itertools import accumulate

cumnumbers2 = accumulate(numbers2, lambda x, y: x*y)

grr = [Int(f"x{i}") for i in range(80)]

s = Solver()
for i in grr:
    s.add(0 <= i)
    s.add(i <= 9)
s.add(
    sum(a*b*i for a, b, i in zip(numbers1, cumnumbers2, grr)) == secret
)
print(s.check())
print(s.model())
print("".join(map(str, [s.model()[i].as_long() for i in grr]))[::-1])

p.interactive()