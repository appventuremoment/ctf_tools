from Crypto.Util.number import *
from string import ascii_letters, digits
from random import choice
from itertools import *
import numpy


for i in range(10000):
	temp = getPrime(128)
	print(temp.bit_length())

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

array = [11, 5629178899781869, 214102045664027531508792298619]
for i in list(powerset(array)):
	print(isPrime(int(numpy.prod(i))))

'''
plain = "".join(choice(ascii_letters + digits) for _ in range(16))

print(plain)

prime1 = getPrime(128)
prime2 = getPrime(128)
mod = prime1 * prime2
power = 65537
key = inverse(power, (prime1 - 1) * (prime2 - 1))

ct = pow(bytes_to_long(plain.encode()), power, mod)
print(ct)

pt = pow(ct, key, mod)

print(long_to_bytes(pt).decode())


cipher = pow(bytes_to_long(plain.encode()), power, mod)

#print(f"{cipher = }")
#print(f"{key = }")



#find it such that e*d = 1 (mod N)

#usually it is pow(cipher, key, mod)
#how find mod

print("input?")
input = input("> ").strip()

if input == plain:
    print("Pass!")
    with open("/challenge/flag.txt") as f:
        print(f.read())
else:
    print("FAILED!")
    with open("/challenge/flag.txt") as f:
        print(f.read())
'''
