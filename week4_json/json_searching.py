# This file was used to exercise the search and find demons as I compile this
# json project...commenting on how things work so that I don't forget...

import json
#this takes in the 'properties' dict, makes a new dict reference,
#then sorts the new dict keys and stores in propKeysList var. then make
#a list from propKeysList. 'id' string is the 5th idx position
#so grab that str and return from method
def wranglingKeys(d):
	newDict = d
	propKeysList = sorted(newDict.keys())
	propKeysList = list(propKeysList)
	searchID = propKeysList[0]
	return searchID
#this method is killing me, i can not for the life me get the
#id number to return...i can print(x) here and it shows the proper
#id, but for some reason the loop messes it up and when i try to 
#store the return val in a new var, it gets None...
def wranglingValues(d):
	newDict = d
	if 1850147310 in newDict.values():
		#print(newDict['id'])
		x = newDict['id']
		print(x)


#open our json file
f = open('cgcapitalprojects_img.geojson.json', 'r')
#load via json module
res = json.load(f)
#for each dictionary in the features list
for p in res['features']:
	#call on wranglingKeys method to get 'id' string
	searchIDkey = wranglingKeys(p['properties'])
	#x = wranglingValues(p['properties']) This new var 'x' will only get None from the method call...
	if p['properties']['area'] == 'Engineering and Construction': #how i am able to obtain the actual id value
		areaID = p['properties']['area']
#create a new dict using just string 'id' and actual number (this will be sent to the json file)
d = {searchIDkey: areaID}
#convert our dict object to JSON object and write to file
json.dump(d, fp=open('testjson.txt', 'w'), indent=4)
print('written to Json file')

anotherD = json.load(open('testjson.txt'))



"""
Find a value from JSON file and write it to file, 
then reopen file w/ Python objs from JSON

#for each dictionary in 'features' dict
for p in res['features']:
	#if the 'properties' dict in 'features' has key 'id' == 1850147310
	if p['properties']['id'] == 1850147310:
		#areaID hold that value
		areaID = p['properties']['id']
		#write the value to json file
		json.dump(p['properties']['id'], fp=open('testjson.txt', 'w'), indent=4)
		print('written to file')
#use json module to load Python objects from JSON format
P = json.load(open('testjson.txt'))
#print out Python objects
print(type(P))
"""