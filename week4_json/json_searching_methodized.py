
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

def AssembleAllLists(dictFromCgCap):
	areaList = []
	assetList = []
	statusList = []
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

def writeResultsJson(whatToFind, comparedToWhat, searchList, compareList):
	finalDict = dict([(whatToFind, searchList), (comparedToWhat, compareList)])
	json.dump(finalDict, open('new_data.txt', 'w'), indent=4)
	print("JSON file written...")

def printSearchResults(searchCriteria, whatToFind, comparedToWhat, searchList, compareList):
	print(searchCriteria, '\t|', whatToFind, '\t|', comparedToWhat)
	for n, g in zip(searchList, compareList):
		print('\t', n, '\t', g)

def main():
	dictFromCgCap = load_JSON()
	uniqueAreaList, uniqueAssetList, uniqueStatusList = AssembleAllLists(dictFromCgCap)
	bigSearchDict = createBigDict(uniqueAreaList, uniqueAssetList, uniqueStatusList)
	dictFromJSONSearch = loadingJson(bigSearchDict)
	searchCriteria, whatToFind, comparedToWhat = enterSearchCriteria(dictFromJSONSearch)
	searchList, compareList = findByJsonKey(dictFromCgCap, searchCriteria, whatToFind, comparedToWhat)
	writeResultsJson(whatToFind, comparedToWhat, searchList, compareList)
	#printSearchResults(searchCriteria, whatToFind, comparedToWhat, searchList, compareList)

main()