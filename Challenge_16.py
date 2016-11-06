#challenge-16 url : http://www.pythonchallenge.com/pc/return/mozart.html

from PIL import Image

im = Image.open('mozart.gif')
width, height = im.size
new = Image.new(im.mode, im.size)

for y in range(height):
	line = [im.getpixel((x, y)) for x in range(width)]
	pink = line.index(195)
	new_line = line[pink:] + line[:pink]
	for x in range(width):
		new.putpixel((x, y),new_line[x])

new.save('new.gif')
