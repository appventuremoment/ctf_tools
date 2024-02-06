from Crypto.Util.number import *
from string import ascii_letters, digits
from random import choice
from itertools import *

#find all factors in sagemath
#attempt to decode the message (catch error of invalid start byte for .decode)

def powerset(iterable):
    #powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


factors = [2, 2, 2, 2, 2, 3, 5, 5, 83, 8783, 20879, 8246599, 810730319639655992646812442683, 5987012576421689270427266369201]
temp = []


for i in list(powerset(factors)):
	product = 11
	for x in i:
		product *= x
	product += 1
	if product.bit_length() == 128 and isPrime(product) and product not in temp:
		temp.append(product)


if len(temp) == 2:
	print("PERFECT")

for x in temp:
	for y in temp:
		p = x
		q = y

		N = p * q

		#CHANGE THIS
		e = 65537
		ct = 43130377066436046460206747706355574020218154468475545415453246750611805439632
		d = 22310885954202696703012429389813789202684828518235997523466625214391253843873

		pt = long_to_bytes(pow(ct, d, N))
		print(pt)
		print(pt.decode())


'''
from Crypto.Util.number import getPrime, inverse, bytes_to_long
from string import ascii_letters, digits
from random import choice

pt = join(choice(ascii_letters + digits) for _ in range(16))
p = getPrime(128)
q = getPrime(128)
N = p * q
e = 65537
d = inverse(e, (p - 1) * (q - 1))

ct = pow(bytes_to_long(pt.encode()), e, N)

print(f"{ct = }")
print(f"{d = }")

print("vainglory?")
vainglory = input("> ").strip()

if vainglory == pt:
    print("Conquered!")
    with open("/challenge/flag.txt") as f:
        print(f.read())
else:
    print("Hubris!")
'''
