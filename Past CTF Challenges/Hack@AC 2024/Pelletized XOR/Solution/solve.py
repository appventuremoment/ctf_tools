from pwn import * 

#From the other file
listofnum = [1, 26, 362, 1351, 18817, 262087, 3650401, 13623482, 138907099, 1013220139, 10002289250, 100000082198, 1000000003127, 10000000001018, 100000000000096, 1000000000000009, 10000000000000000, 100000000000000000, 1100000000000000000, 10000000000000000000, 100000000000000000000, 1100000000000000000000, 10000000000000000000000, 110000000000000000000000, 1100000000000000000000000, 10000000000000000000000000, 110000000000000000000000000, 1100000000000000000000000000, 10000000000000000000000000000, 110000000000000000000000000000, 1100000000000000000000000000000, 11000000000000000000000000000000, 100000000000000000000000000000000, 1100000000000000000000000000000000, 10000000000000000000000000000000000, 100000000000000000000000000000000000, 1100000000000000000000000000000000000, 10000000000000000000000000000000000000, 100000000000000000000000000000000000000, 1100000000000000000000000000000000000000, 10000000000000000000000000000000000000000, 100000000000000000000000000000000000000000, 1100000000000000000000000000000000000000000, 10000000000000000000000000000000000000000000, 100000000000000000000000000000000000000000000, 1100000000000000000000000000000000000000000000, 11000000000000000000000000000000000000000000000, 100000000000000000000000000000000000000000000000, 1100000000000000000000000000000000000000000000000, 11000000000000000000000000000000000000000000000000, 100000000000000000000000000000000000000000000000000, 1100000000000000000000000000000000000000000000000000, 11000000000000000000000000000000000000000000000000000, 100000000000000000000000000000000000000000000000000000, 1100000000000000000000000000000000000000000000000000000, 11000000000000000000000000000000000000000000000000000000, 100000000000000000000000000000000000000000000000000000000, 1100000000000000000000000000000000000000000000000000000000, 11000000000000000000000000000000000000000000000000000000000, 100000000000000000000000000000000000000000000000000000000000, 1100000000000000000000000000000000000000000000000000000000000, 10000000000000000000000000000000000000000000000000000000000000, 110000000000000000000000000000000000000000000000000000000000000, 1100000000000000000000000000000000000000000000000000000000000000, 10000000000000000000000000000000000000000000000000000000000000000]

def xor(x, y):
    return [a^b for a, b in zip(x, y)]


r = connect('beta.hackac.live', 3001)

key = r.recv()
print(key.decode())
# #Key is:
# 51 8 7 42 31 42 38 3 53 43 43 60 15 56 40 46 8 15 9 63 8 56 28 62 30 0 44 2 33 56 13 57 64 64 5 56 19 53 36 6 51 5 51 52 2 58 25 43 51 57

# Give me 50 numbers, space separated:

key = key.decode().split(' ')[1:-6]
key[0] = key[0][4:]
key = [int(x) for x in key]

print(key)
#[51, 8, 7, 42, 31, 42, 38, 3, 53, 43, 43, 60, 15, 56, 40, 46, 8, 15, 9, 63, 8, 56, 28, 62, 30, 0, 44, 2, 33, 56, 13, 57, 64, 64, 5, 56, 19, 53, 36, 6, 51, 5, 51, 52, 2, 58, 25, 43, 51, 57]

test = []
input = ''
for i in key:
    input += str(listofnum[i]) + ' '
    test.append(math.floor(math.log(listofnum[i], 10)))


print(test) #Making sure that the inputs match the key
#[51, 8, 7, 42, 31, 42, 38, 3, 53, 43, 43, 60, 15, 56, 40, 46, 8, 15, 9, 63, 8, 56, 28, 62, 30, 0, 44, 2, 33, 56, 13, 57, 64, 64, 5, 56, 19, 53, 36, 6, 51, 5, 51, 52, 2, 58, 25, 43, 51, 57]

r.sendline(bytes(input, 'utf-8'))
out = r.recv()
print(out.decode())
#You passed! Is this correct though...
# [65, 67, 83, 73, 123, 99, 48, 78, 103, 114, 65, 116, 53, 95, 117, 95, 77, 97, 53, 84, 51, 82, 101, 68, 95, 84, 72, 101, 95, 112, 51, 108, 49, 95, 101, 113, 85, 97, 116, 49, 48, 78, 33, 95, 102, 106, 50, 51, 100, 125]
r.close()


out = out.decode().split(' ')[5:]
out[0] = out[0][11:]
out[-1] =  out[-1][:-2]
out = [int(x) for x in ''.join(out).split(',')]

print(''.join([chr(x) for x in out]))







