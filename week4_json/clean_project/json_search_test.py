
import json

def AssembleAreaList(d):
	item = d['area']
	areaList.append(item)

def AssembleStatusList(d):
	item = d['status']
	statusList.append(item)

def AssembleAssetList(d):
	item = d['asset_type']
	assetList.append(item)

def findByJsonKey(d, whatToFind, comparedToWhat):
	for value in d.values():
		if value == searchCriteria:
			searchList.append(d[whatToFind])
			compareList.append(d[comparedToWhat])

def removeEmptyValFromAreaList(uniqueAreaList):
	for x in uniqueAreaList:
		if x == '':
			uniqueAreaList.remove(x)

def printListValues(uniqueList):
	for item in uniqueList:
		print(item)

def AssembleAllLists():
	for p in dictFromCgCap['features']:
		AssembleAreaList(p['properties'])
		AssembleAssetList(p['properties'])
		AssembleStatusList(p['properties'])


#these lists contain our unique vals
areaList = []	
assetList = []
statusList = []
#this list holds what we searched for
searchList = []
compareList = []
#open our geojson file
cgCapFile = open('cgcapitalprojects_img.geojson.json', 'r')
#use json module to load geojson file (json -> python objects)
dictFromCgCap = json.load(cgCapFile)
#call method to assemble list of area, asset, status values
AssembleAllLists()
#use list() and set() to filter unique area, asset, and status values
uniqueAreaList = list(set(areaList))
uniqueAssetList = list(set(assetList))
uniqueStatusList = list(set(statusList))
#take the empty space out of area list
removeEmptyValFromAreaList(uniqueAreaList)
#make a dictionary of unique area, asset_type, status. each 
#string (area, asset_type, status) maps to a list of unique vals
bigSearchDict = dict(area=uniqueAreaList, asset_type=uniqueAssetList, status=uniqueStatusList)
#dump the unique dictionary to data.txt
json.dump(bigSearchDict, open('data.txt', 'w'), indent=4)
#print('written to data.txt') #test
#open data.txt (our unique vals in JSON format)
jsonSearchFile = open('data.txt', 'r')
#load the data.txt json to python dict object (dictFromJSONSearch)
dictFromJSONSearch = json.load(jsonSearchFile)
#user decides to search by area, status, or asset_type
searchCategory = input('Enter search criteria (area, status, asset_type) >> ')
#load whichever selected list into searchValues
searchValues = dictFromJSONSearch[searchCategory]
#sort the list so it prints out in same order each time program runs
searchValues.sort()
for value in searchValues: print(value)
#get next search criteria. (ex. if status, select from in prog., canceled, planned, completed)
searchCriteria = input('Which %s to search by? >> ' % (searchCategory))
options = """
id, status, asset_type, asset_id, area, start_date, area,
task_description, budgeted_amount, fiscal_year, inactive, name	
"""
print(options)
#search for any comparative option. (ex user selects status: canceled, then whatToFind = id, 
#will return a search of all id #'s from properties w/ status: canceled')
whatToFind = input('Enter value to find for all %s >> ' % (searchCriteria))
#another value, find all ids that are canceled for a certain area, status, or asset_type
comparedToWhat = input('Enter next value >> ')
#loop through geojson dict of 'features'
for p in dictFromCgCap['features']:
	#findByJsonKey loops through each 'properties' dict searching based on user conditions
	findByJsonKey(p['properties'], whatToFind, comparedToWhat)

#reportDict = dict(zip(searchList, compareList))
reportDict = dict(whatToFind=searchList, comparedToWhat=compareList)
#reportList = reportDict[whatToFind]
print(searchCriteria, '\t|', whatToFind, '\t|', comparedToWhat)
#!!!! CRITICAL! What I originally did above was dict(zip()) into reportDict
#however when i would print the dict by key value, any duplicate numbers
#from the json file would be removed...to avoid this, use zip and iterate through
#the unique tuples created.  this allows something like budget and year to be printed
#for a certain asset_types....before, if records had the same budget, it 
#did not make the dictionary...
for n, g in zip(searchList, compareList):
	print('\t\t', n, '\t\t', '\t\t', g)




#print('-' * 20)
#print('%s %s %s' % (searchCriteria, whatToFind, comparedToWhat))
#print('-' * 20)
#for report in reportDict:
#	print(report, reportDict[report])

#for item in searchList:
#	if item == '':
#		print('%s: none' %(whatToFind))
#	else:	
#		print('%s: %s' % (whatToFind, str(item)))



"""
Another Draft so that I dont forget the use of the uniqueAreaDicionary
and other empty dictionaries (see assemble_uniquevalues.py..or something
like that...)

import json

def AssembleAreaList(d):
	item = d['area']
	areaList.append(item)

def AssembleStatusList(d):
	item = d['status']
	statusList.append(item)

def AssembleAssetList(d):
	item = d['asset_type']
	assetList.append(item)


def findByJsonKey(d, whatToFind):
	for value in d.values():
		if value == searchCriteria:
			searchList.append(d[whatToFind])

def removeEmptyValFromAreaList(uniqueAreaList):
	for x in uniqueAreaList:
		if x == '':
			uniqueAreaList.remove(x)

def printListValues(uniqueList):
	for item in uniqueList:
		print(item)

def AssembleAllLists():
	for p in dictFromCgCap['features']:
		AssembleAreaList(p['properties'])
		AssembleAssetList(p['properties'])
		AssembleStatusList(p['properties'])


#these lists contain our unique vals
areaList = []	
assetList = []
statusList = []
#this list holds what we searched for
searchList = []
#these empty dicts will be used to create objects to dump into json file
#uniqueAreaDictionary = {}
#uniqueAssetDictionary = {}
#uniqueStatusDictionary = {}
#open test json search criteria
#jsonSearchFile = open('testjson.txt', 'r')################################### JSON SEARCH TEST
#open our geojson file
cgCapFile = open('cgcapitalprojects_img.geojson.json', 'r')
#use json module to load search criteria (json -> python object)
#dictFromJSONSearch = json.load(jsonSearchFile)#################################### JSON SEARCH TEST
#use json module to load geojson file (json -> python objects)
dictFromCgCap = json.load(cgCapFile)
#grab value from basic json search criteria contained in 'testjson.txt'
#valueFromJSONSearch = dictFromJSONSearch['area']#######################################JSON SEARCH TEST
#call method to assemble list of area, asset, status values
AssembleAllLists()
#use list() and set() to filter unique area, asset, and status values
uniqueAreaList = list(set(areaList))
uniqueAssetList = list(set(assetList))
uniqueStatusList = list(set(statusList))
#take the empty space out of area list
removeEmptyValFromAreaList(uniqueAreaList)
#populate empty unique dictionarys, will be used to write to json search file
#uniqueAreaDictionary.setdefault('area', uniqueAreaList)
#uniqueAssetDictionary.setdefault('asset_type', uniqueAssetList)
#uniqueStatusDictionary.setdefault('status', uniqueStatusList)
bigSearchDict = dict(area=uniqueAreaList, asset_type=uniqueAssetList, status=uniqueStatusList)
#this dumps the unique dictionary to data.txt, going to try
#and retrieve this later for search specifications...
json.dump(bigSearchDict, open('data.txt', 'w'), indent=4)
print('written to data.txt')
jsonSearchFile = open('data.txt', 'r')
dictFromJSONSearch = json.load(jsonSearchFile)

searchCategory = input('Enter search criteria (area, status, asset_type) >> ')
searchValues = dictFromJSONSearch[searchCategory]
searchValues.sort()
print(', '.join(searchValues))
searchCriteria = input('Which criteria? >> ')
options = """
#id, status, asset_type, asset_id, area, start_date, area,
#task_description, budgeted_amount, fiscal_year, inactive, name
"""
print(options)
whatToFind = input('What to find? >> ')

for p in dictFromCgCap['features']:
	findByJsonKey(p['properties'], whatToFind)

print('-' * 20)
print('%s %s' % (searchCriteria, whatToFind))
print('-' * 20)
for item in searchList:
	if item == '':
		print('%s: none' %(whatToFind))
	else:	
		print('%s: %s' % (whatToFind, str(item)))

#End other draft
"""



"""
Commented Code first Draft

import json
# this method takes in the properties dict on each loop
# and iterates through each value. If the value from our 
# JSON search criteeria is a match, append the id # from
# that property to the properyIDList.  The list will
# contain all ID numbers for properties with area type 'Engineering and Construction' 
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

#End first draft	
"""