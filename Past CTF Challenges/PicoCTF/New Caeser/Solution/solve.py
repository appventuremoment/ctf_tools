import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

def rev_shift(e, k):
	t1 = ord(e) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 - t2) % len(ALPHABET)]

def b16_decode(cypher):
	cypher = [cypher[i:i+2] for i in range(0, len(cypher), 2)]
	dec = ""
	for pair in cypher:
		part1 = ALPHABET.index(pair[0])
		part2 = ALPHABET.index(pair[1])
		binarynumber = "{0:04b}".format(part1) + "{0:04b}".format(part2)
		dec += chr(int(binarynumber, 2))
	return dec

ct = "kjlijdliljhdjdhfkfkhhjkkhhkihlhnhghekfhmhjhkhfhekfkkkjkghghjhlhghmhhhfkikfkfhm"
for x in range(16):
    enc = ""
    for i, c in enumerate(ct):
        enc += rev_shift(c, ALPHABET[x])
    print(b16_decode(enc))