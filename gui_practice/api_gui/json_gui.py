import tkinter
import json

class make_stuff():
	
	def __init__(self):
		self.main_window = tkinter.Tk()
		self.main_window.title('Json Program')
		self.search_label = tkinter.Label(self.main_window, text='Enter Search Criteria (area, status, asset_type)')
		self.search_entry = tkinter.Entry(self.main_window)
		self.search_button = tkinter.Button(self.main_window, text='Search')
		self.quit_button = tkinter.Button(self.main_window, text='Quit', command=self.main_window.destroy)
		self.search_entry.focus_set()
		self.search_label.grid(row=0, column=0)
		self.search_entry.grid(row=1, column=0, sticky='NSEW')
		self.search_button.grid(row=2, column=0, sticky='NSEW')
		self.quit_button.grid(row=3, column=0, sticky='NSEW')
		tkinter.mainloop()

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
		print() #new line for formatting
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

	def writeResultsJson(searchCriteria, whatToFind, comparedToWhat, searchList, compareList):
		anotherDict = dict([(whatToFind, searchList), (comparedToWhat, compareList)]) # neat way to build a dicts
		finalDict = dict([(searchCriteria, anotherDict)]) # build a dict w/ the searchCriteria as key, values are what use3r wants to look for, ex id, budgeted_amount
		json.dump(finalDict, open('new_data.txt', 'w'), indent=4)
		print("JSON file written...")

	def printSearchResults(searchCriteria, whatToFind, comparedToWhat, searchList, compareList):
		print(searchCriteria, '\t|', whatToFind, '\t|', comparedToWhat)
		for n, g in zip(searchList, compareList):
			print('\t', n, '\t', g)

#def main():
	#new_goo = make_gui()
	"""
	try:
		dictFromCgCap = load_JSON()
		uniqueAreaList, uniqueAssetList, uniqueStatusList = AssembleAllLists(dictFromCgCap)
		bigSearchDict = createBigDict(uniqueAreaList, uniqueAssetList, uniqueStatusList)
		dictFromJSONSearch = loadingJson(bigSearchDict)
		searchCriteria, whatToFind, comparedToWhat = enterSearchCriteria(dictFromJSONSearch)
		searchList, compareList = findByJsonKey(dictFromCgCap, searchCriteria, whatToFind, comparedToWhat)
		writeResultsJson(searchCriteria, whatToFind, comparedToWhat, searchList, compareList)
	except:	
		print("Sorry, something went wrong with the search...please check user entry.")
	printSearchResults(searchCriteria, whatToFind, comparedToWhat, searchList, compareList)
	"""
#main()