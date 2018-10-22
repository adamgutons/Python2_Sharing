from bs4 import BeautifulSoup
import requests
import json
import webbrowser


def generateSession():		# generate our web session, url is english wikipedia API
	session = requests.Session()
	URL = "https://en.wikipedia.org/w/api.php"
	return session, URL

def whoToSearch():
	whoToSearch = input("Who to search? >> ")
	return whoToSearch

# i had a real bitch of a time collecting the api request and sorting...wiki_revisions.py will show that i was iterating through
# a loop of ppl names from people.txt and dumping the api data into a file.  however, it was not dumping ONE unique dictionary for ALL persons
# in the search list...i.e. one donald dict, another hillary dict, in the same file...calling on json.load threw an error...too complicated
# for my brainlet self to work through....SO....I make a few different methods...this one grabs 20 of the oldest of edits to the page Donald Trump
#...obviously generateNewTrump() gets 20 of the most recent........we return the file to pass to gatherComments() method
def generateOldComments(whoToSearch, session, URL):
	fileString = 'old_data.txt' 	
	dataFile = open(fileString, 'w')
	
	params = {
		'action': "query",
		'titles': whoToSearch,
		'format': "json",
		'prop': "revisions",
		'rvprop': 'user|comment|timestamp',
		'rvlimit': '50',
		'rvdir': 'newer'
		#'rvstart':'2016-11-09T00:00:00Z',
		#'rvend':'2016-11-08T00:00:00Z', #year, month, day
	}
	response = session.get(url=URL, params=params)
	dataDict = response.json()
	json.dump(dataDict, dataFile, indent=4) #store our search in a file
	print('old rev. comments written to file...')
	print()
	return fileString

# same method, just for newer revision comments
def generateNewComments(whoToSearch, session, URL):
	fileString = 'new_data.txt' 	
	dataFile = open(fileString, 'w')

	params = {
		'action': "query",
		'titles': whoToSearch,
		'format': "json",
		'prop': "revisions",
		'rvprop': 'user|comment|timestamp',
		'rvlimit': '50',
		'rvdir': 'older'
		#'rvstart':'2016-11-09T00:00:00Z',
		#'rvend':'2016-11-08T00:00:00Z', #year, month, day
	}
	response = session.get(url=URL, params=params)
	dataDict = response.json()
	json.dump(dataDict, dataFile, indent=4) #store our search in a file
	print('new rev. comments written to file...')
	print()
	return fileString

# pass in the file string name so it is more mobile and can get 'r' priveleges
# we look through the standard API 'query''pages' dicts to get to the page id
# and finally the 'revisions' key, which has a list value.  the list contains
# dicitionarys w/ individual revision info.  one of the keys is 'comment', which
# is what we want to add to our empty commentList and spit back out
def gatherComments(fileString):
	commentList = []
	newFile = open(fileString, 'r')
	newDict = json.load(newFile)
	searchingText = newDict['query']['pages'] 
	for page in searchingText:
		revisionList = searchingText[page]['revisions']
	for revision in revisionList:
		if revision['comment'] != '' and len(revision['comment']) > 1:
			commentList.append(revision['comment'])
	return commentList

def buildWebpage(who, oldCommentList, newCommentList):
	soup = BeautifulSoup('<head></head><body></body>', "lxml") #gets a basic <html><body><div> page started
	relTag = soup.new_tag("link") # make a new link tag
	relTag.attrs["rel"] = "stylesheet" #edit the rel attributes to tell page link is a css stylesheet
	relTag.attrs["href"] = "webpage.css"
	soup.head.append(relTag)

	oldCommentsDiv = soup.new_tag("div", id="oldComments") #make a div to contain old comments
	soup.body.append(oldCommentsDiv)
	head_tag = soup.new_tag("h1") # create a header tag
	head_tag.string = who + " oldest revision comments" # header tag will be person searched for, plus old or new comments
	oldCommentsDiv.append(head_tag) # put the header tag in our main div class

	#iterate trhough old comment list, creating a p tag each time and appending the comment text
	#to the tag.  insert after the first header tag
	for comment in oldCommentList:
		anotherTag = soup.new_tag("p")
		anotherTag.string = comment
		head_tag.insert_after(anotherTag)
	
	#create a new div to hold old comments and give it a class slector "oldComments"
	#append the new div to our soup body
	newCommentsDiv = soup.new_tag("div", id="newComments")
	soup.body.append(newCommentsDiv)

	head_tag = soup.new_tag("h1")
	head_tag.string = who + " newest revision comments"
	newCommentsDiv.append(head_tag)

	for comment in newCommentList:
		anotherTag = soup.new_tag("p")
		anotherTag.string = comment
		head_tag.insert_after(anotherTag)	

	prettySoup = soup.prettify()
	print(prettySoup)
	htmlFile = open('webpage.html', 'w')
	htmlFile.write(prettySoup)
	webbrowser.open('webpage.html') #opens our webpage right away...neat!
	
def main():
	session, URL = generateSession()
	who = whoToSearch()
	oldFileString = generateOldComments(who, session, URL)
	newFileString = generateNewComments(who, session, URL)
	oldCommentList = gatherComments(oldFileString)
	newCommentList = gatherComments(newFileString)
	buildWebpage(who, oldCommentList, newCommentList)

main()