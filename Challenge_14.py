#challenge-14 url : http://www.pythonchallenge.com/pc/return/italy.html

from PIL import Image

n = 0
x = 0
y = 0
flag = 0    
num = 1
max = 99

im = Image.open('wire.png')
new_im = Image.new(im.mode, (100,100))

PIC = [im.getpixel((z, 0)) for z in range(10000)]
	
for i in range(10000):
	new_im.putpixel((x,y), PIC[n])
	if flag == 0:
		x += 1
	elif flag == 1:
		y += 1
	elif flag == 2:
		x -= 1
	elif flag == 3:
		y -= 1

	if num == max:
		flag += 1
		num = 1
		#print n
		if flag == 4:
			flag = 0
			max -= 2
			x += 1
			y += 1
	else:
		num += 1
	
	n += 1
	
new_im.save('pic.png')
