from bs4 import BeautifulSoup
import urllib.request
import csv

def generateSearchURL(): # input what you want to search, append this string to wikipedias search URL and return it
	search = input('Search >> ')
	base = "https://www.wikipedia.org/wiki/"
	return base + search

def setResponsesURL(searchURL): # with the search URL constructed, make a URL requested to the page, store the response, read response and return it
	req = urllib.request.Request(searchURL)
	resp = urllib.request.urlopen(req)
	resp_data = resp.read()
	return resp_data

def getSomeSoup(resp_data): # print or write soup data to csv file
	l = []
	soup = BeautifulSoup(resp_data, 'html.parser')
	for headline in soup.find_all('span', class_="mw-headline"): # find span elements w/ mw-headline class
		readOut = headline.text #get the text of each element and store in readOut variable
		l.append(readOut) # add to list
		#print(readOut) # print if we want
		with open('names.csv', 'w', newline='') as csvfile: # open a csv file
			spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|') # create a csv writer
			spamwriter.writerow(l) # need to write list object, so take l and write the whole thing
	print('csv written')		

def main():
	searchURL = generateSearchURL()	
	resp_data = setResponsesURL(searchURL)
	getSomeSoup(resp_data)
	
main()