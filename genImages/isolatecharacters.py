from PIL import Image,ImageDraw
import os
def isolate_characters():
    #beware 5-6-7-8-9 dont have images for them
    basepath = os.getcwd() 
    alphFile = {
    'a':'2','b':'77','c':'48','d':'22','e':'5','f':'66','g':'0','h':'28','i':'14','j':'99'
    ,'k':'16','l':'1','m':'11','n':'60','o':'56','p':'24','q':'267','r':'25','s':'15',
    't':'188','u':'23','v':'4','w':'100','x':'33','y':'34','z':'92'
    ,'0':'169','1':'3','2':'193','3':'1091','4':'424','9':'36'}

    transparent = (0,0,0,0)
    black = (0,0,0,255)
    for character,filename in alphFile.items():
        img = Image.open(basepath + "\\characters_source\\" + filename +'.png')
        bgcolor = img.getpixel((0,0))
        drawer = ImageDraw.Draw(img)
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                if img.getpixel((i,j)) == bgcolor:
                    drawer.point((i,j), fill = transparent)
                else:
                    drawer.point((i,j), fill = black)
        img.save(basepath +'\\characters\\'+character +'.png')