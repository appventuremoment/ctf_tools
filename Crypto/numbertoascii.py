numbers = [268, 413, 438, 313, 426, 337, 272, 188, 392, 338, 77, 332, 139, 113, 92, 239, 247, 120, 419, 72, 295, 190, 131]
out = ""
for i in numbers:
	temp = pow(i, -1, 41)
	if temp < 26:
		out += chr(temp + 96)
	elif temp == 37:
		out += "_"
	else:
		temp -= 27
		out += str(temp)

print(out)


import string

alphabet = string.ascii_lowercase

alphabet += "0123456789_"
flag_enc = [104, 85, 69, 354, 344, 50, 149, 65, 187, 420, 77, 127, 385, 318, 133, 72, 206, 236, 206, 83, 342, 206, 370]

flag = ""
for c in flag_enc:
    pos = pow(c, -1, 41)
    flag += alphabet[pos - 1]

print(flag)
