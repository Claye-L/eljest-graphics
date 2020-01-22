from PIL import Image
from os import listdir

baseImg = Image.open('CSGORosters_200121.png')

#split into team rectangles
for row in range(0,6):
	for column in range(0,10):
		img = baseImg
		left = column*176
		top = row*176
		teamImg = img.crop((left,top,left + 177,top + 177))
		teamImg.save('subimages\\{0}_{1}.png'.format(row,column))
		
teamimagepaths = listdir('subimages')

counter = 0
for path in teamimagepaths:
	img = Image.open('subimages\\'+path)
	for row in range(0,5):
		left = 15
		right = 33
		top= 71 + row * 20
		bottom = 89 + row * 20
		ball = img.crop((left,top,right,bottom))
		ball.save('countryballs\\' + str(counter) + '.png')
		counter += 1