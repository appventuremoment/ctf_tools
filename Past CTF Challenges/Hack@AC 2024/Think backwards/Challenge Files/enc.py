flag = open('flag.txt', 'r').read()

enc = ''
for i, char in enumerate(flag):
    if i==0:
        enc += hex(ord(char))[2:]
    else:
        if i%2==0: # if i is divisible by 2
            enc += hex(ord(char) + 15)[2:]
        else:
            enc += hex(ord(char) - 15)[2:]

with open('out.txt', 'w') as out:
    out.write(enc)
