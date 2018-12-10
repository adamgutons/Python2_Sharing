import tkinter
import api_gui

def make_main():
	root = tkinter.Tk()
	root.title('Python II Final')
	api_button = tkinter.Button(root, text='API Program', command=make_api)
	json_button = tkinter.Button(root, text='Json Program')
	rps_button = tkinter.Button(root, text='Rock, Paper, Scissors')
	files_button = tkinter.Button(root, text='View Program Files')
	quit_button = tkinter.Button(root, text='Quit', command=root.destroy)
	title_label = tkinter.Label(root, text='Welcome to my Python II Final GUI Program', pady=10)
	title_label.grid(row=0, column=0, columnspan=2)
	api_button.grid(row=1, column=0, columnspan=2, sticky='NSEW') # sticky is where widget "sticks", we specify by direction north south east or west
	json_button.grid(row=2, column=0, columnspan=2, sticky='NSEW')
	rps_button.grid(row=3, column=0, columnspan=2, sticky='NSEW')
	files_button.grid(row=4, column=0, columnspan=2, sticky='NSEW')
	quit_button.grid(row=5, column=0, columnspan=2, sticky='NSEW')
	#rps_button.grid(row=2, column=0)
	tkinter.mainloop()

def make_api():
	new goo = api_gui.make_gui()

def main():
	make_main()

main()