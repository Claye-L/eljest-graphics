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
img.show()