import re
from pwn import *

def subs(test):
	if test == '000':
		return '100'
	elif test == '001':
		return '110'
	elif test == '010':
		return '111'
	elif test == '011':
		return '101'
	elif test == '100':
		return '001'
	elif test == '101':
		return '010'
	elif test == '110':
		return '011'
	elif test == '111':
		return '000'

def XOR(input, message):
	print(input, message)
	output = ['0'] * 3
	for x in range(3):
		if input[x] == '1' and message[x] == '1':
			output[x] = '0'
		elif input[x] == '1' and message[x] == '0':
			output[x] = '1'
		elif input[x] == '0' and message[x] == '1':
			output[x] = '1'

	return "".join(output)


inp = "000000110111010000111110100111011000"
IV = "100"

#out: 110000
#IV = "001"
#inp = "000001"

inp = re.findall("...?", inp)
print(IV, inp)
output = []

for i in range(len(inp)):
	if i == 0:
		temp = XOR(IV, inp[i])
	else:
		temp = XOR(inp[i], output[i - 1])
	output.append(subs(temp))


print("".join(output))
