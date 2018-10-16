import requests
import json

#response = requests.get("https://en.wikipedia.org/w/api.php")

def generateSession():
	S = requests.Session()
	URL = "https://en.wikipedia.org/w/api.php"
	params = {
		'action': "query",
		'titles': "Robert Anton Wilson",
		'format': "json",
		'prop': "images",
	}
	response = S.get(url=URL, params=params)
	data = response.json()
	return data

def writeJsonFile(data):
	json.dump(data, open('wiki_api_json.txt', 'w'), indent=4) #store our search in a file
	print('api query written to file...')
	print() # spacing for console output

def outPutWikiImg(data):
	wikiDict = data['query']['pages'] # create a smaller dict using wiki api return keys/vals
	print("-" * 24) #format console output
	print("Images in wiki article |")
	print("-" * 24)
	for ID in sorted(wikiDict): #['26056']['images']:
		# print(ID)  prints an id number associated w/ the image api search
		for item in (wikiDict[ID]['images']): # iterate through ID num dict by 'images'
			for key in item: #each image is in a dict w/ k: 'title' v:'file' and k: 'ns': v:6
				#print(item)
				if isinstance(item[key], str): # check to see if value is a string (file name)
					imageFile = item[key].lstrip('File:')
					print(imageFile)

def main():
	data = generateSession()
	writeJsonFile(data)
	outPutWikiImg(data)

main()

#for work on 'titles': "Albert Einstein"
#for i in range(len(data['query']['pages']['736']['images'])):
#	print(data['query']['pages']['736']['images'][i]['title'])

#print(response.status_code)