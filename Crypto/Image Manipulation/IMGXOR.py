from PIL import Image
from pwn import *

im = Image.open('1.png', 'r')
width, height = im.size
print(width, height)
flag_pixel = list(im.getdata())


im = Image.open("2.png", "r")
width, height = im.size
lem_pixel = list(im.getdata())
#print(lem_pixel)

flag = []
a, b, c = 0, 0, 0
for x in range(len(flag_pixel)):
	for y in range(3):
		if y == 0:
			a = flag_pixel[x][0] ^ lem_pixel[x][0]
		elif y == 1:
			b = flag_pixel[x][1] ^ lem_pixel[x][1]
		else:
			c = flag_pixel[x][2] ^ lem_pixel[x][2]
	flag.append((a, b, c))


print(len(flag))
#CHANGE DIMENSIONS
im = Image.new('RGB', (width, height))
im.putdata(flag)
im.save("flagout.png")
