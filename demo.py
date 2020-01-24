from PIL import Image,ImageColor
from draw import draw_string,draw_country_ball

country_size =(18,18)
character_size = (13,16)

img = Image.new('RGBA',(140,220),ImageColor.getcolor('black','RGBA'))

country_codes = ['ee','fr','nl','se','se','ar','ru','se','se','us','us']
names = ['vinss','claye','thevug','eljest','hannah','metalgio','raintnt','smolbean','emma','kevin','staar']
white = (255,255,255)

row_spacing = 20
for i in range(len(names)):
    country = country_codes[i]
    name = names[i]
    draw_country_ball(img,(4,i * row_spacing),country)
    draw_string(img,(26,i*row_spacing),name,white)
img.save('demo.png')
#img.show()

gif_images = list()
#gif making
for i in range(len(names)):
	country = country_codes[i]
	name = names[i]
	img = Image.new('RGBA',(140,20),ImageColor.getcolor('black','RGBA'))
	draw_country_ball(img,(4,0),country)
	draw_string(img,(26,0),name,white)
	gif_images.append(img)

img.save('demo.gif', save_all=True, append_images=gif_images, optimize=False, duration=320, loop=0)