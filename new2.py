import os

home = os.environ.get("HOMEDRIVE")


guitar_path = home + os.sep + "NewTopic"

fender = guitar_path + os.sep + 'Fender'
gibson = guitar_path + os.sep + 'Gibson'
yamaha = guitar_path + os.sep + 'Yamaha'
fender_telecaster = fender + os.sep + "Telecaster"
gibson_les_paul = gibson + os.sep + "Les Paul"
fender_roy = fender_telecaster + os.sep + "Roy Buchanan"
fender_merle = fender_telecaster + os.sep + "Merle Haggard"
fender_merle_disc = fender_merle + os.sep + "Discography"

paths_list = [guitar_path, fender, gibson, yamaha, fender_telecaster, gibson_les_paul, fender_roy, fender_merle, fender_merle_disc]

for paths in paths_list:
	os.mkdir(paths)