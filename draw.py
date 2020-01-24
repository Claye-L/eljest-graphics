from PIL import Image, ImageColor
import os 
import numpy as np
dir_path = os.path.dirname(os.path.realpath(__file__)) + "\\genImages"
transparent = (0,0,0,0)

country_size =(18,18)
character_size = (13,16)

def get_character_path(char):
    return dir_path + "\\characters\\" + char +'.png'
def get_country_path(country):
    return dir_path + "\\countries\\" + country +'.png'

def replace_black(image, color):
    #code copied from https://stackoverflow.com/questions/3752476/python-pil-replace-a-single-rgba-color
    data = np.array(image)   # "data" is a height x width x 4 numpy array
    red, green, blue, alpha = data.T # Temporarily unpack the bands for readability
    # Replace white with red... (leaves alpha values alone...)
    black_areas = (red == 0) & (blue == 0) & (green == 0)
    data[..., :-1][black_areas.T] = color[0],color[1],color[2] # Transpose back needed
    im2 = Image.fromarray(data)
    return im2

def draw_character(image, xy, char, color):
    cimg = Image.open(get_character_path(char))
    if(color is not None):
        cimg = replace_black(cimg,color)
    image.paste(cimg,xy,cimg)
    return 

def draw_country_ball(image,xy, country):
    cimg = Image.open(get_country_path(country))
    image.paste(cimg,xy,cimg)
    return

def draw_string(image,xy,string, color=None):
    for i in range(len(string)):
        char = string[i]
        if(char == ' '):
            continue
        else:
            draw_character(image,(xy[0] + 12*i, xy[1]),char,color)