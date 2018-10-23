
import json

def AssembleAreaList(d, areaList):
	item = d['area']
	areaList.append(item)
	return areaList

def AssembleStatusList(d, statusList):
	item = d['status']
	statusList.append(item)
	return statusList

def AssembleAssetList(d, assetList):
	item = d['asset_type']
	assetList.append(item)
	return assetList

def removeEmptyValFromAreaList(uniqueAreaList):
	for x in uniqueAreaList:
		if x == '':
			uniqueAreaList.remove(x)

def printListValues(uniqueList):
	for item in uniqueList:
		print(item)

def load_JSON():
	cgCapFile = open('cgcapitalprojects_img.geojson.json', 'r')
	dictFromCgCap = json.load(cgCapFile)
	return dictFromCgCap

def createUniqueLists(l):
	uniqueList = list(set(l))
	return uniqueList

def AssembleAllLists(dictFromCgCap, areaList, assetList, statusList):
	for p in dictFromCgCap['features']:
		uniqueAreaList = createUniqueLists(AssembleAreaList(p['properties'], areaList))	
		uniqueAssetList = createUniqueLists(AssembleAssetList(p['properties'], assetList))
		uniqueStatusList = createUniqueLists(AssembleStatusList(p['properties'], statusList))
		removeEmptyValFromAreaList(uniqueAreaList)
	return uniqueAreaList, uniqueAssetList, uniqueStatusList 

def createBigDict(uniqueAreaList, uniqueAssetList, uniqueStatusList):
	bigSearchDict = dict(area=uniqueAreaList, asset_type=uniqueAssetList, status=uniqueStatusList)
	return bigSearchDict

def loadingJson(bigSearchDict):
	json.dump(bigSearchDict, open('data.txt', 'w'), indent=4)
	jsonSearchFile = open('data.txt', 'r')
	dictFromJSONSearch = json.load(jsonSearchFile)
	return dictFromJSONSearch

def enterSearchCriteria(dictFromJSONSearch):
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
	return searchCriteria, whatToFind, comparedToWhat

def findByJsonKey(dictFromCgCap, searchCriteria, whatToFind, comparedToWhat):
	searchList = []
	compareList = []
	for p in dictFromCgCap['features']:
		for i in p['properties'].values():
			if i == searchCriteria:
				searchList.append(p['properties'][whatToFind])
				compareList.append(p['properties'][comparedToWhat]) 
	return searchList, compareList

def printSearchResults(searchCriteria, whatToFind, comparedToWhat, searchList, compareList):
	print(searchCriteria, '\t|', whatToFind, '\t|', comparedToWhat)
	#!!!! CRITICAL! What I originally did above was dict(zip()) into reportDict
	#however when i would print the dict by key value, any duplicate numbers
	#from the json file would be removed...to avoid this, use zip and iterate through
	#the unique tuples created.  this allows something like budget and year to be printed
	#for a certain asset_types....before, if records had the same budget, it 
	#did not make the dictionary b/c dictionary keys are UNIQUE
	for n, g in zip(searchList, compareList):
		print('\t', n, '\t', g)

def main():
	areaList = []	
	assetList = []
	statusList = []
	#searchList = []
	#compareList = []
	#cgCapFile = open('cgcapitalprojects_img.geojson.json', 'r')
	dictFromCgCap = load_JSON()
	uniqueAreaList, uniqueAssetList, uniqueStatusList = AssembleAllLists(dictFromCgCap, areaList, assetList, statusList)
	#uniqueAreaList = list(set(areaList))
	#uniqueAssetList = list(set(assetList))
	#uniqueStatusList = list(set(statusList))
	#removeEmptyValFromAreaList(uniqueAreaList)
	bigSearchDict = createBigDict(uniqueAreaList, uniqueAssetList, uniqueStatusList)
	#bigSearchDict = dict(area=uniqueAreaList, asset_type=uniqueAssetList, status=uniqueStatusList)
	dictFromJSONSearch = loadingJson(bigSearchDict)
	searchCriteria, whatToFind, comparedToWhat = enterSearchCriteria(dictFromJSONSearch)
	searchList, compareList = findByJsonKey(dictFromCgCap, searchCriteria, whatToFind, comparedToWhat)
	printSearchResults(searchCriteria, whatToFind, comparedToWhat, searchList, compareList)
	#json.dump(bigSearchDict, open('data.txt', 'w'), indent=4)
	#jsonSearchFile = open('data.txt', 'r')
	#dictFromJSONSearch = json.load(jsonSearchFile)
	#searchCategory = input('Enter search criteria (area, status, asset_type) >> ')
	#searchValues = dictFromJSONSearch[searchCategory]
	#searchValues.sort()
	#for value in searchValues: print(value)
	#searchCriteria = input('Which %s to search by? >> ' % (searchCategory))
	#print(options)
	#whatToFind = input('Enter value to find for all %s >> ' % (searchCriteria))
	#comparedToWhat = input('Enter next value >> ')
	#for p in dictFromCgCap['features']:
	#	findByJsonKey(p['properties'], whatToFind, comparedToWhat)
	#print(searchCriteria, '\t|', whatToFind, '\t|', comparedToWhat)
	#!!!! CRITICAL! What I originally did above was dict(zip()) into reportDict
	#however when i would print the dict by key value, any duplicate numbers
	#from the json file would be removed...to avoid this, use zip and iterate through
	#the unique tuples created.  this allows something like budget and year to be printed
	#for a certain asset_types....before, if records had the same budget, it 
	#did not make the dictionary b/c dictionary keys are UNIQUE
	#for n, g in zip(searchList, compareList):
	#	print(n, g)

main()