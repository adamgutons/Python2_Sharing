import tkinter

class MyGUI:
	def __init__(self):	# __init__ called when MyGUI object is constructed in main
		self.main_window = tkinter.Tk()
		tkinter.mainloop()

def main():
	my_gui = MyGUI()

main()