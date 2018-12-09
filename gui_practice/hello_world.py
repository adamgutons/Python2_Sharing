import tkinter

class MyGUI:
	def __init__(self):
		self.main_window = tkinter.Tk()

		self.main_window.geometry('200x100')
		self.label = tkinter.Label(self.main_window, text="I'M SLEEPY") # we pass in the widget we want the label to belong to, self.main_window

		self.label_new = tkinter.Label(self.main_window, text="and I be high")
		self.label.pack()
		self.label_new.pack()

		tkinter.mainloop()


def main():

	gui_fool = MyGUI()

main()