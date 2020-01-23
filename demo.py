from PIL import Image,ImageColor
from draw import draw_string,draw_country_ball

country_size =(18,18)
character_size = (13,16)

img = Image.new('RGBA',(110,140),ImageColor.getcolor('white','RGBA'))

country_codes = ['ee','fr','nl','se','se']
names = ['vinss','claye','thevug','eljest','hannah']

row_offset = 28
for i in range(len(names)):
    country = country_codes[i]
    name = names[i]
    draw_country_ball(img,(4,i * row_offset),country)
    draw_string(img,(26,i*row_offset),name)
img.save('demo.png')