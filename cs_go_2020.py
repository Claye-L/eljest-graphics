from PIL import Image, ImageColor, ImageDraw
from draw import draw_string, draw_country_ball, FontSize, draw_centered_string
import csv
import os
from itertools import groupby

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

country_size =(18,18)
character_size = (13,16)
big_char_size = (24,31)
team_card_size = 226
country_left, country_top = 14,80
title_left,title_top =18,19
text_left,text_top = 34,83
row_height = 20

with open('csteams1.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    players = [row for row in csv_reader]
# df = pandas.read_csv('csteams1.csv')
# print(df)
# teams = df.groupby(['team'])
# print(teams)
teams = list()
for team,players in groupby(players, lambda x: x["team"]):
    p = list(players)
    teams.append({"team":team,"players": p,"color":p[0]["color"],"fill":p[0]["fill"]})
def draw_team_card(img, draw, xy, team):
    start_left,start_top = xy
    #draw background rectangle
    draw.rectangle((xy[0] + 8, xy[1] + 8, xy[0] + team_card_size - 2, xy[1] + team_card_size - 2),team["fill"],(0,0,0,255),3)
    #draw team title
    draw_centered_string(img, (start_left + 10, start_top + title_top, start_left + 220, start_top + 31), 
        team["team"], color= ImageColor.getcolor(team["color"],"RGBA"), fontsize= FontSize.Normal)
    #draw each player country/name
    for i in range(len(team["players"])):
        player = team["players"][i]
        draw_country_ball(img,(start_left + country_left, start_top + country_top + i * row_height),player["country"])
        draw_string(img,(start_left + text_left, start_top + text_top + i * row_height), player["player"], ImageColor.getcolor(team["color"],"RGBA"))

teams_per_row = 8
image = Image.new('RGBA',(team_card_size * teams_per_row, team_card_size * 8),ImageColor.getcolor('white','RGBA'))
draw = ImageDraw.Draw(image)

#draw_team_card(image,draw,(0,0),teams[0])

for i in range(len(teams)):
    draw_team_card(image,draw,((i % teams_per_row) * team_card_size, team_card_size * (i // teams_per_row)),teams[i])

image.save('cs2020.png')
image.show()