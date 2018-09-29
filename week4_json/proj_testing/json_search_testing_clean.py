
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

areaList = []	
assetList = []
statusList = []
searchList = []
compareList = []
cgCapFile = open('cgcapitalprojects_img.geojson.json', 'r')
dictFromCgCap = json.load(cgCapFile)
AssembleAllLists()
uniqueAreaList = list(set(areaList))
uniqueAssetList = list(set(assetList))
uniqueStatusList = list(set(statusList))
removeEmptyValFromAreaList(uniqueAreaList)
bigSearchDict = dict(area=uniqueAreaList, asset_type=uniqueAssetList, status=uniqueStatusList)
json.dump(bigSearchDict, open('data.txt', 'w'), indent=4)
jsonSearchFile = open('data.txt', 'r')
dictFromJSONSearch = json.load(jsonSearchFile)
searchCategory = input('Enter search criteria (area, status, asset_type) >> ')
searchValues = dictFromJSONSearch[searchCategory]
searchValues.sort()
for value in searchValues: print(value)
searchCriteria = input('Which %s to search by? >> ' % (searchCategory))
options = """
id, status, asset_type, asset_id, area, start_date, area,
task_description, budgeted_amount, fiscal_year, inactive, name	
"""
print(options)
whatToFind = input('Enter value to find for all %s >> ' % (searchCriteria))
comparedToWhat = input('Enter next value >> ')
for p in dictFromCgCap['features']:
	findByJsonKey(p['properties'], whatToFind, comparedToWhat)
print(searchCriteria, '\t|', whatToFind, '\t|', comparedToWhat)
for n, g in zip(searchList, compareList):
	print(n, g)
