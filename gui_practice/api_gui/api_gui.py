# attempting to gui-fy this api script as part of my fall semester final 2018 @ ccac for python2 taught by eric darsow
from bs4 import BeautifulSoup
import requests
import json
import webbrowser
import tkinter

class make_gui():
	def __init__(self):
		self.main_window = tkinter.Tk()
		self.main_window.title('API Project')
		#self.main_window.geometry('300x200')
		#self.top_frame = tkinter.Frame(self.main_window)
		#self.top_frame.config(bd=1, bg='BLACK') # using this to tinker w/ widget sizes
		#self.mid_frame = tkinter.Frame(self.main_window)
		#self.mid_frame.config(bd=1, bg='YELLOW') # using this to tinker w/ widget sizes
		#self.bottom_frame = tkinter.Frame(self.main_window)
		#self.bottom_frame.config(bd=10,bg='BLUE') # using this to tinker w/ widget sizes
		self.entry_label = tkinter.Label(self.main_window, text='Who to search?')
		self.value = tkinter.StringVar() # make a stringvar() to display any text in the error_label
		self.error_label = tkinter.Label(self.main_window, wraplength=300) # make a label to display any errors,
		self.entry_label.grid(row=0, padx=5, sticky='E')																# wraplength is measure in pixels
		self.api_entry = tkinter.Entry(self.main_window)
		self.api_entry.focus_set() # sets cursor in entry widget as soon as window loads
		#self.entry_label.pack(expand=True)
		self.error_label.grid(column=0, row=1, columnspan=2, padx=10)
		self.api_entry.grid(row=0, column=1, padx=5)
		self.search_button = tkinter.Button(self.main_window, text='Generate Webpage', command=self.buildWebpage)
		self.quit_button = tkinter.Button(self.main_window, text='Quit', command=self.main_window.destroy)
		self.search_button.grid(row=0, column=2)
		self.quit_button.grid(row=1, column=2, sticky='NSEW')
		#self.top_frame.pack()
		#self.mid_frame.pack()
		#self.bottom_frame.pack()
		self.main_window.bind('<Return>', self.buildWebpage)
		tkinter.mainloop()


	def generateSession(self):		# generate our web session, url is english wikipedia API
		session = requests.Session()
		URL = "https://en.wikipedia.org/w/api.php"
		return session, URL
	
	#def whoToSearch():
	#	whoToSearch = self.api_entry.get()
	#	return whoToSearch

	def generateOldComments(self, whoToSearch, session, URL):
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
			#'rvend':'2016-11-08T00:00:00Z' #year, month, day
		}
		response = session.get(url=URL, params=params)
		dataDict = response.json()
		json.dump(dataDict, dataFile, indent=4) #store our search in a file
		print('old rev. comments written to file...')
		print()
		return fileString

	# same method, just for newer revision comments
	def generateNewComments(self):
		whoToSearch = self.api_entry.get()
		session, URL = self.generateSession()
		oldComments_fileString = self.generateOldComments(whoToSearch, session, URL)
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
			#'rvstart':'2017-11-09T00:00:00Z',
			#'rvend':'2017-11-08T00:00:00Z' #year, month, day
		}
		response = session.get(url=URL, params=params)
		dataDict = response.json()
		json.dump(dataDict, dataFile, indent=4) #store our search in a file
		print('new rev. comments written to file...')
		#print()
		return fileString, oldComments_fileString	

	def gatherComments(self, fileString):
		#fileString = self.generateNewComments()
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

	def buildWebpage(self, event=None):
		try:
			self.error_label.config(text='') #resets gui error log if there is one
			newComments_fileString, oldComments_fileString = self.generateNewComments()
			oldCommentList = self.gatherComments(oldComments_fileString)
			newCommentList = self.gatherComments(newComments_fileString)
			who = self.api_entry.get()
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
		except:
			print('error')
			self.error_label.config(text='Something went wrong...changing search case can help...')

	def close_gui():
		self.main_window.destroy()