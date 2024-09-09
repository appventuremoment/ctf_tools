with open('Past CTF Challenges/PicoCTF/C3/Solution/outp.py') as f:
    chars = f.read()

b = 1
for i in range(len(chars)):
    if i == b ** 3:
        print(chars[i])
        b += 1