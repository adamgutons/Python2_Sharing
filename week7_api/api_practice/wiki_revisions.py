import requests
import json

#response = requests.get("https://en.wikipedia.org/w/api.php")
def getNames():
	peopleList = []
	for person in open('people.txt'):
		peopleList.append(person.rstrip('\n'))
	return peopleList


def generateSession(peopleList):
	S = requests.Session()
	URL = "https://en.wikipedia.org/w/api.php"
	for person in peopleList:
		#print(person)
		params = {
			'action': "parse",
			'titles': person,
			'format': "json",
			'prop': "revisions",
			'rvprop': 'user|comment|timestamp',
			'rvlimit': 20,
			'rvstart':'2016-11-09T00:00:00Z',
			'rvend':'2016-11-08T00:00:00Z', #year, month, day
		}
		response = S.get(url=URL, params=params)
		data = response.json()
		json.dump(data, open('revision_data.txt', 'a'), indent=4) #store our search in a file
	print('api query written to file...')

def writeJsonFile(data):
	json.dump(data, open('revision_data.txt', 'a'), indent=4) #store our search in a file
	print('api query written to file...')
	print() # spacing for console output

	
def main():
	peopleList = getNames()
	generateSession(peopleList)

main()

