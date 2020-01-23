import os
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
folderstomake = ['characters','characters_source',"countryballs",'subimages','countries','country_sources']

for folder in folderstomake:
	if(not os.path.exists(folder)):
		os.mkdir(folder)
		
from splitIntoLetters import split_into_letters
from isolateuniquecountries import isolate_unique_countries
from cropcountryballs import crop_country_balls

split_into_letters()
crop_country_balls()
isolate_unique_countries()