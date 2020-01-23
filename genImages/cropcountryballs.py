from PIL import Image, ImageDraw
from os import listdir,chdir
chdir('C:\\Users\\Claye_L\\source\\repos\\eljest-graphics\\genImages')
imgpaths = listdir('countryballs')
transparentAdress = [6,4,3,2,1,1]

transparent = (0,0,0,0)

for path in imgpaths:
    img = Image.open('countryballs\\' + path).copy()
    drawer = ImageDraw.Draw(img)
    height,width = img.size
    for i in range(len(transparentAdress)):
        length = transparentAdress[i]
        points=[(i,0),(i,length-1)]
        drawer.line(points,fill =transparent)

        points = [(17-i,0),(17-i,length-1)]
        drawer.line(points,fill = transparent)

        points = [(i,17),(i,17 - length +1)]
        drawer.line(points,fill=transparent)

        points = [(17 - i,17),(17-i,17- length + 1)]
        drawer.line(points,fill=transparent)
    img.save('country_sources\\' + path)
