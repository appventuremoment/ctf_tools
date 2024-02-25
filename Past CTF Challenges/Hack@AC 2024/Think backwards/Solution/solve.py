inp = '4134623a8a5343547a684f6373646e648366725c6e227c5077245b618c'
splitinp = [inp[i:i+2] for i in range(0, len(inp), 2)]

print(splitinp)

out = ''

for i,char in enumerate(splitinp):
    char = int(char, 16)
    if i==0:
        out += chr(char)
    else:
        if i%2==0: # if i is divisible by 2
            out += chr(char - 15)
        else:
            out += chr(char + 15)

print(out)