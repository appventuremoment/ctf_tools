# import Image
from PIL import Image
import re

with open("WheelOfFortune.txt") as file:
    inp = file.read()
    inp = re.sub('[\[\],]', '', inp).split(' ')

inp = [list(map(int, inp[x:x+3])) for x in range(0, len(inp) - 2, 3)]

print(len(inp))


width = 843
height = 1499

# factordb
i3 = Image.new('RGB', (width, height))


count = 0
for i in range(width):
    for j in range(height):
        i3.putpixel((i,j), tuple(inp[count]))
        count += 1

# save the image
print('Done!')
i3.save("output.png", "PNG")

