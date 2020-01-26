from PIL import Image, ImageColor
from enum import Enum
import os 
import numpy as np
dir_path = os.path.dirname(os.path.realpath(__file__)) + "\\genImages"
transparent = (0,0,0,0)

country_size =(18,18)
character_size = (12,16)
character_big_size=(24,31)

class FontSize(Enum):
    Normal = ""
    Big = "_big"
def get_character_path(char, fontsize):
    return dir_path + "\\characters" + fontsize.value + "\\" + char +'.png'
def get_country_path(country):
    return dir_path + "\\countries\\" + country +'.png'

def char_width_for_font(fontsize):
    if fontsize == FontSize.Normal:
        return character_size[0]
    elif fontsize == FontSize.Big:
        return character_big_size[0]

def replace_black(image, color):
    #code copied from https://stackoverflow.com/questions/3752476/python-pil-replace-a-single-rgba-color
    data = np.array(image)   # "data" is a height x width x 4 numpy array
    red, green, blue, alpha = data.T # Temporarily unpack the bands for readability
    # Replace white with red... (leaves alpha values alone...)
    black_areas = (red == 0) & (blue == 0) & (green == 0)
    data[..., :-1][black_areas.T] = color[0],color[1],color[2] # Transpose back needed
    im2 = Image.fromarray(data)
    return im2

def draw_character(image, xy, char, color, fontsize = FontSize.Normal):
    try:
        cimg = Image.open(get_character_path(char,fontsize))
    except FileNotFoundError:
        return
    if(color is not None):
        cimg = replace_black(cimg,color)
    image.paste(cimg,xy,cimg)
    return 

def draw_country_ball(image,xy, country):
    cimg = Image.open(get_country_path(country))
    image.paste(cimg,xy,cimg)
    return

def draw_centered_string(image, xybox, text, color = None, fontsize = FontSize.Normal):
    if fontsize == FontSize.Normal:
        char_width = character_size[0]
    elif fontsize == FontSize.Big:
        char_width = character_big_size[0]
    center = (xybox[2] - xybox[0]) //2
    textcenter = len(text) * char_width // 2
    offset = center - textcenter
    draw_string(image, (xybox[0] + offset, xybox[1], xybox[2], xybox),
        text, color, fontsize)


def draw_string(image,xy, text, color=None, fontsize = FontSize.Normal):
    for i in range(len(text)):
        char = text[i]
        if(char == ' '):
            continue
        else:
            draw_character(image,(xy[0] + char_width_for_font(fontsize) * i, xy[1]),char,color, fontsize)