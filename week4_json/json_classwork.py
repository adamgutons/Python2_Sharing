import json

def splitDict(d):
	for x in d:
		print(x + ':', d[x])

def logMalformedProject(d):
	datafile.write(str(d['id']))
	print('Data written to file')

def AssembleList(d):
	item = d['area']
	l.append(item)
	
l = []
datafile = open('data.txt', 'w')
f = open('cgcapitalprojects_img.geojson.json', 'r')
res = json.load(f)
for p in res['features']:
	splitDict(p['properties'])
	AssembleList(p['properties'])
	if p['properties']['area'] == '':
		logMalformedProject(p['properties'])
uniqueAreaVals = list(set(l))
for x in uniqueAreaVals:
	print(x)

"""
Commented Code

import json

# this method prints the properties dict key value pairs
def splitDict(d):
	for x in d:
		print(x + ':', d[x])
#this method writes the id of an empty area value for any 
#property dict to a data.txt file
def logMalformedProject(d):
	datafile.write(str(d['id']))
	print('Data written to file')
#this method takes value of each property area and stores in 
#list l
def AssembleList(d):
	item = d['area']
	l.append(item)
#create list l
l = []
#create file to write id #s to
datafile = open('data.txt', 'w')
#create object containing json file	
f = open('cgcapitalprojects_img.geojson.json', 'r')
#use json module to load dicts into res
res = json.load(f)
#loop through each property in the dict features 
for p in res['features']:
	#call method to prind property dict k,v pairs
	splitDict(p['properties'])
	#call method to assemble each property area val into a list
	AssembleList(p['properties'])
	#if area key in any property dict is empty, call method
	#to write the id of that property area to data.txt
	if p['properties']['area'] == '':
		logMalformedProject(p['properties'])
#create a variable that first creates a set from our area key 
#values list (ex. Engineering and Construction). This clears
#any duplicate objects in the list.  Then we pass this 
#set to list() to get a list of unique area key values.
#Prints unique values to the console
uniqueAreaVals = list(set(l))
for x in uniqueAreaVals:
	print(x)
"""	