from bs4 import BeautifulSoup
import urllib.request
import csv

def generateSearchURL(): # input what you want to search, append this string to wikipedias search URL and return it
	search = input('Search >> ')
	search = search.replace(' ', '_') # needed for replacing spaces, so searching by name
	base = "https://www.wikipedia.org/wiki/"
	return base + search

def setResponsesURL(searchURL): # with the search URL constructed, make a URL requested to the page, store the response, read response and return it
	req = urllib.request.Request(searchURL)
	resp = urllib.request.urlopen(req)
	resp_data = resp.read()
	return resp_data

def getSomeSoup(resp_data, searchURL): # print or write soup data to csv file
	linkList = []
	baseList = []
	linkDict = {}
	soup = BeautifulSoup(resp_data, 'html.parser')
	for link in soup.find_all('span', class_="tocnumber"):
		linkList.append(link.parent.attrs ['href'].lstrip('#'))

	for l in linkList:
		linkDict[l] = searchURL + '#' + l # gives us link to topic inner page...wikipedia is badass 
										  # b/c pretty much any search criteria will match, uppercase, lower, etc
	for k in linkDict:
		print('-' * 20)
		print(k, '||', linkDict[k])
		print('-' * 20)
		#with open('names.csv', 'w', newline='') as csvfile: # open a csv file
		#	spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|') # create a csv writer
		#	spamwriter.writerow(l) # need to write list object, so take l and write the whole thing
	#print('csv written')		

def main():
	searchURL = generateSearchURL()	
	try:
		resp_data = setResponsesURL(searchURL)
		getSomeSoup(resp_data, searchURL)
	except:
		print("Sorry, something went wrong with your search...please try again")
main()