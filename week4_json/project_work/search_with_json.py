import json

def findByJsonKey(d):
	for value in d.values():
		if valueFromJSONSearch == value:
			properyIDList.append(d['id'])

properyIDList = []

jsonSearchFile = open('testjson.txt', 'r')
cgCapFile = open('cgcapitalprojects_img.geojson.json', 'r')


dictFromJSONSearch = json.load(jsonSearchFile)
dictFromCgCap = json.load(cgCapFile)
valueFromJSONSearch = dictFromJSONSearch['area']

for p in dictFromCgCap['features']:
	findByJsonKey(p['properties'])

for ID in properyIDList:
	print('Engineering and Construction ID: ', ID)	

"""
Commented Code

import json
# this method takes in the properties dict on each loop
# and iterates through each value. If the value from our 
# JSON search criteeria is a match, append the id # from
# that property to the properyIDList 
def findByJsonKey(d):
	for value in d.values():
		if valueFromJSONSearch == value:
			properyIDList.append(d['id'])

#create a container to hold our ids from the findByJsonKey method
properyIDList = []

#open files to hold json search criteria, one for our large json file
jsonSearchFile = open('testjson.txt', 'r')
cgCapFile = open('cgcapitalprojects_img.geojson.json', 'r')

# create a dictionary object from our json criteria file & cgcap json file
dictFromJSONSearch = json.load(jsonSearchFile)
dictFromCgCap = json.load(cgCapFile)

# take the value from search criteria, in this case 'Engineering and Construction'
valueFromJSONSearch = dictFromJSONSearch['area']

# iterate over main dict to explore 'properties' with findByJsonKey method
for p in dictFromCgCap['features']:
	findByJsonKey(p['properties'])

# print out the id's that we found
print(properyIDList)	
"""