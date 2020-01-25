from PIL import Image, ImageDraw
import os

def isolate_big_characters():
	teams = ['ast','fnatic','mouz','liquid','eg','100t','vit','navi'
	,'nip','faze','ence','mibr','g2','og','furia','vp','rngds','dig'
	,'north','heroic','tyloo','vp2','gl','vici','hrt','gdsnt','cr4zy'
	,'big','geng','col','forze','sharks','lyon','splyce','smash'
	,'intz','wst','illumi','sprout','legion','cloud9','arcy',
	'spirit','hr','syman','riders','ndnb','pro100','gambit',
	'chaos','btrg','ep','avant','mythic','riot','unique','nfinit'
	,'euni','nemiga','ago']

	transparent = (0,0,0,0)
	black = (0,0,0,255)
	char_height = 31
	char_width = 24

	for i in range(len(teams)):
		file = os.getcwd() + '\\subimages\\'+ str(i) +'.png'
		team = teams[i]
		#characters are not aligned the same if even/odd number of letters
		#if even number, then 92 is start of char index len/2
		#if odd number, then 92 is middle of char index len/2 + 1
		if(len(team) % 2 == 0):
			first_char_start = 92 - (char_width) * (len(team) // 2)
		else:
			first_char_start = 92 - 12 - (char_width) *(len(team) // 2)
		img = Image.open(file)
		for j in range(len(team)):
			filename = os.getcwd() + '\\characters_big\\' + team[j] +'.png'
			if(os.path.isfile(filename)):
				continue
			left =first_char_start + char_width * j
			charimg = img.crop((left, 18, left + char_width, 18+ char_height))
			bgcolor = charimg.getpixel((0,0))
			drawer = ImageDraw.Draw(charimg)
			for i in range(charimg.size[0]):
				for j in range(charimg.size[1]):
					if charimg.getpixel((i,j)) == bgcolor:
						drawer.point((i,j), fill = transparent)
					else:
						drawer.point((i,j), fill = black)
			charimg.save(filename)
