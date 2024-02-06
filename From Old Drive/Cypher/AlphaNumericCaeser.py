import string
import collections

for shift_value in range(36):
	original = string.ascii_uppercase + string.digits
	'''
	shifter = collections.deque(string.ascii_uppercase)
	shifer.rotate(shift_value)
	shifter_uppercase - "".join(list(shifter))

	shifter = collections.deque(string.digits)
	shifter.rotate(shift_value)
	shifter_digits = "".join(list(shifter))
	'''
	shifter = collections.deque(original)
	shifter.rotate(shift_value)
	shifted_original = "".join(list(shifter))

	#change txt here
	with open("output.txt") as filp:
		contents = filp.read()

	flag = []
	for chara in contents:
		if chara in original:
			position = original.index(chara)
			flag.append(shifted_original[position])

		else:
			flag.append(chara)


	print("".join(flag))
