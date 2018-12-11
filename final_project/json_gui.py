import tkinter
import json

class make_stuff():
	
	def __init__(self):
		self.options = "Administration/Sub-Award, Engineering and Construction, Facility Improvement, Neighborhood and Community Development"
		self.area_options = "id, status, asset_type, asset_id, area, start_date, area, task_description, budgeted_amount, fiscal_year, inactive, name"
		self.main_window = tkinter.Toplevel()
		self.main_window.title('Json Program')
		self.search_label = tkinter.Label(self.main_window, text='Enter Search Criteria (area, status, asset_type)')
		self.error_label = tkinter.Label(self.main_window, wraplength=300)
		self.area_label = tkinter.Label(self.main_window, text=self.options, wraplength=300)
		self.options_label = tkinter.Label(self.main_window, text=self.area_options, wraplength=300)
		self.search_entry = tkinter.Entry(self.main_window)
		self.area_entry = tkinter.Entry(self.main_window)
		self.param_label_1 = tkinter.Label(self.main_window, text='Param 1')
		self.param_label_2 = tkinter.Label(self.main_window, text='Param 2')
		self.param_entry_1 = tkinter.Entry(self.main_window)
		self.param_entry_2 = tkinter.Entry(self.main_window)
		self.search_button = tkinter.Button(self.main_window, text='Search', command=self.do_it_all)
		self.quit_button = tkinter.Button(self.main_window, text='Quit', command=self.main_window.destroy)
		self.search_entry.focus_set()
		#self.main_window.bind('<Return>', self.do_it_all)
		self.search_label.grid(row=0, column=0, columnspan=2)
		self.search_entry.grid(row=1, column=0, columnspan=2, sticky='NSEW')
		self.area_label.grid(row=2, column=0, columnspan=2)
		self.area_entry.grid(row=3, column=0, columnspan=2, sticky='NSEW')
		self.options_label.grid(row=4, column=0, columnspan=2)
		self.param_label_1.grid(sticky='W')
		self.param_label_2.grid(sticky='W')
		self.param_entry_1.grid(row=5, column=1, sticky='NSEW')
		self.param_entry_2.grid(row=6, column=1, sticky='NSEW')
		self.search_button.grid(row=7, column=0, columnspan=2, sticky='NSEW')
		self.quit_button.grid(row=8, column=0, columnspan=2, sticky='NSEW')
		self.error_label.grid(row=9, column=0, columnspan=2)
		tkinter.mainloop()

	def AssembleAreaList(self, d, areaList):
		item = d['area']
		areaList.append(item)
		return areaList

	def AssembleStatusList(self, d, statusList):
		item = d['status']
		statusList.append(item)
		return statusList

	def AssembleAssetList(self, d, assetList):
		item = d['asset_type']
		assetList.append(item)
		return assetList

	def removeEmptyValFromAreaList(self, uniqueAreaList):
		for x in uniqueAreaList:
			if x == '':
				uniqueAreaList.remove(x)

	def printListValues(self, uniqueList):
		for item in uniqueList:
			print(item)

	def load_JSON(self):
		cgCapFile = open('cgcapitalprojects_img.geojson.json', 'r')
		dictFromCgCap = json.load(cgCapFile)
		return dictFromCgCap

	def createUniqueLists(self, l):
		uniqueList = list(set(l))
		return uniqueList

	def AssembleAllLists(self, dictFromCgCap):
		areaList = []
		assetList = []
		statusList = []
		for p in dictFromCgCap['features']:
			uniqueAreaList = self.createUniqueLists(self.AssembleAreaList(p['properties'], areaList))	
			uniqueAssetList = self.createUniqueLists(self.AssembleAssetList(p['properties'], assetList))
			uniqueStatusList = self.createUniqueLists(self.AssembleStatusList(p['properties'], statusList))
			self.removeEmptyValFromAreaList(uniqueAreaList)
		return uniqueAreaList, uniqueAssetList, uniqueStatusList 

	def createBigDict(self, uniqueAreaList, uniqueAssetList, uniqueStatusList):
		bigSearchDict = dict(area=uniqueAreaList, asset_type=uniqueAssetList, status=uniqueStatusList)
		return bigSearchDict

	def loadingJson(self, bigSearchDict):
		json.dump(bigSearchDict, open('data.txt', 'w'), indent=4)
		jsonSearchFile = open('data.txt', 'r')
		dictFromJSONSearch = json.load(jsonSearchFile)
		return dictFromJSONSearch

	def enterSearchCriteria(self):
		searchCategory = self.search_entry.get()
		#searchCategory = input('Enter search criteria (area, status, asset_type) >> ')
		#searchValues = dictFromJSONSearch[searchCategory]
		#searchValues.sort()
		#for value in searchValues: print(value)
		#print() #new line for formatting
		searchCriteria = self.area_entry.get()
		#print(options)
		whatToFind = self.param_entry_1.get()
		comparedToWhat = self.param_entry_2.get()
		print(searchCriteria, whatToFind, comparedToWhat, searchCategory)
		return searchCriteria, whatToFind, comparedToWhat

	def findByJsonKey(self, dictFromCgCap, searchCriteria, whatToFind, comparedToWhat):
		searchList = []
		compareList = []
		for p in dictFromCgCap['features']:
			for i in p['properties'].values():
				if i == searchCriteria:
					searchList.append(p['properties'][whatToFind])
					compareList.append(p['properties'][comparedToWhat]) 
		return searchList, compareList

	def writeResultsJson(self, searchCriteria, whatToFind, comparedToWhat, searchList, compareList):
		anotherDict = dict([(whatToFind, searchList), (comparedToWhat, compareList)]) # neat way to build a dicts
		finalDict = dict([(searchCriteria, anotherDict)]) # build a dict w/ the searchCriteria as key, values are what use3r wants to look for, ex id, budgeted_amount
		json.dump(finalDict, open('json_data.txt', 'w'), indent=4)
		print("JSON file written...")

	def printSearchResults(self, searchCriteria, whatToFind, comparedToWhat, searchList, compareList):
		print(searchCriteria, '\t|', whatToFind, '\t|', comparedToWhat)
		for n, g in zip(searchList, compareList):
			print('\t', n, '\t', g)

	def do_it_all(self):
		try:
			searchCriteria, whatToFind, comparedToWhat = self.enterSearchCriteria()
			print(searchCriteria, whatToFind, comparedToWhat)
			dictFromCgCap = self.load_JSON()
			uniqueAreaList, uniqueAssetList, uniqueStatusList = self.AssembleAllLists(dictFromCgCap)
			bigSearchDict = self.createBigDict(uniqueAreaList, uniqueAssetList, uniqueStatusList)
			dictFromJSONSearch = self.loadingJson(bigSearchDict)
			searchCriteria, whatToFind, comparedToWhat = self.enterSearchCriteria()
			searchList, compareList = self.findByJsonKey(dictFromCgCap, searchCriteria, whatToFind, comparedToWhat)
			self.writeResultsJson(searchCriteria, whatToFind, comparedToWhat, searchList, compareList)
			self.error_label.config(text='Json file wrote to disk...')
		except:	
		#	print("Sorry, something went wrong with the search...please check user entry.")
			self.error_label.config(text='Sorry, something went wrong with the search...please check user entry.')
