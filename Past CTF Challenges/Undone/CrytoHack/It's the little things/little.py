from Crypto.Util.number import *
from random import randint

p = getPrime(1024)

flag = b"""???"""

n = p*p

g = getPrime(512)*p + 1

#n = p ** 2
#g = pq + 1
#A = binomial series of (pq + 1) ** flag mod  p ** 2
#A = flag * pq + 1

a = bytes_to_long(flag)

A = pow(g,a,n)

print(g)
print(A)
