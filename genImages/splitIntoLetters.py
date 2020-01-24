from PIL import Image
from os import listdir

def split_into_letters():
	baseImg = Image.open('CSGORosters_200121.png')
	counter = 0
	#split into team rectangles
	for row in range(0,6):
		for column in range(0,10):
			img = baseImg
			left = column*176
			top = row*176
			teamImg = img.crop((left,top,left + 177,top + 177))
			teamImg.save('subimages\\{0}.png'.format(counter))
			counter += 1
	teamimagepaths = listdir('subimages')

	#countryballs
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
			
	counter = 0
	for path in teamimagepaths:
		img = Image.open('subimages\\'+path)
		for row in range(0,5):
			for column in range(0,11):
				left = 34 + 12*column
				right = 47 + 12*column
				top= 73 + row * 20
				bottom = 89 + row * 20
				character = img.crop((left,top,right,bottom))
				character.save('characters_source\\' + str(counter) + '.png')
				counter += 1