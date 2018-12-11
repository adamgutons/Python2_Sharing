import tkinter
import api_gui
import json_gui
import rps_gui

class make_main():
	def __init__(self):	
		self.root = tkinter.Tk()
		self.root.title('Python II Final')
		self.title_label = tkinter.Label(self.root, text='Welcome to my Python II Final GUI Program', pady=10)
		self.api_button = tkinter.Button(self.root, text='API Program', command=self.make_api)
		self.json_button = tkinter.Button(self.root, text='Json Program', command=self.make_json)
		self.rps_button = tkinter.Button(self.root, text='Rock, Paper, Scissors', command=self.make_rps)
		self.files_button = tkinter.Button(self.root, text='View Program Files')
		self.quit_button = tkinter.Button(self.root, text='Quit', command=self.root.destroy) # w/ other objects acting on Toplevel(), closing this menu closes them all
		self.title_label.grid(row=0, column=0, columnspan=2)
		# sticky is where widget "sticks", we specify by direction north south east or west
		self.api_button.grid(row=1, column=0, columnspan=2, sticky='NSEW') 
		self.json_button.grid(row=2, column=0, columnspan=2, sticky='NSEW')
		self.rps_button.grid(row=3, column=0, columnspan=2, sticky='NSEW')
		self.files_button.grid(row=4, column=0, columnspan=2, sticky='NSEW')
		self.quit_button.grid(row=5, column=0, columnspan=2, sticky='NSEW')
		#rps_button.grid(row=2, column=0)
		tkinter.mainloop()

	def make_api(self):
		api_goo = api_gui.make_gui()

	def make_json(self):
		json_goo = json_gui.make_stuff()

	def make_rps(self):
		rps_goo = rps_gui.make_rps()


def main():
	main_gui = make_main()

main()