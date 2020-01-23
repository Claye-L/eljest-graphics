from PIL import Image
import os 
dir_path = os.path.dirname(os.path.realpath(__file__)) + "\\genImages"
transparent = (0,0,0,0)

country_size =(18,18)
character_size = (13,16)

def get_character_path(char):
    return dir_path + "\\characters\\" + char +'.png'
def get_country_path(country):
    return dir_path + "\\countries\\" + country +'.png'

def draw_character(image, xy, char):
    cimg = Image.open(get_character_path(char))
    image.paste(cimg,xy,cimg)
    return 

def draw_country_ball(image,xy, country):
    cimg = Image.open(get_country_path(country))
    image.paste(cimg,xy,cimg)
    return

def draw_string(image,xy,string):
    for i in range(len(string)):
        char = string[i]
        if(char == ' '):
            continue
        else:
            draw_character(image,(xy[0] + 13*i, xy[1]),char)