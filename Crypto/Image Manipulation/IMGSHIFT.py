# THIS IS FOR SHIFTING EACH ROW OF PIXELS IN AN IMAGE BY DIFFERENT AMOUNTS
# SUCH THAT THE FIRST PIXEL OF EACH ROW IS A SPECIFIC COLOUR

from PIL import Image

im = Image.open("1.png", "r")
pixels = list(im.getdata())
print(pixels[0]) #gets the pixel at top left, reference for which pixel needs to be first for each row


im = Image.open("2.png", "r")
width, height = im.size
pixels = list(im.getdata())
#print(width, height)


#splitting list of all pixels into 2d list of pixels (such that each sublist is a row)
#CHANGE DIMENSIONS
flag = []
for i in range(height):
	flag.append(pixels[i * width: i * width + width])

#for each sublist (x), looks for the refernce pixel, then shifts them into the right position
out2 = []
for x in flag:
	for y in range(len(x)):
		#CHANGE PIXEL REFERENCED
		if x[y] == (255, 0, 255, 255):
			temp = x[y:] + x[:y]
			out2.append(temp)
			break

#change 2d list back to a list such that it can be written back into an image
out = []
for x in out2:
	for y in x:
		out.append(y)


#CHANGE DIMENSIONS
im = Image.new('RGB', (width, height))
im.putdata(out)
im.save("flagout.png")
