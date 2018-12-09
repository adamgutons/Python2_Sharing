import tkinter

class Frame_GUI:
	def __init__(self):

		self.main_window = tkinter.Tk()

		self.top_frame = tkinter.Frame(self.main_window)
		self.bottom_frame = tkinter.Frame(self.main_window)

		self.label1 = tkinter.Label(self.top_frame, text='Top label 1')
		self.label2 = tkinter.Label(self.top_frame, text='Top label 2')
		self.label3 = tkinter.Label(self.top_frame, text='Top label 3')

		self.label1.pack(side='top')
		self.label2.pack(side='top')
		self.label3.pack(side='top')

		self.label4 = tkinter.Label(self.top_frame, text='Bottom label 1')
		self.label5 = tkinter.Label(self.top_frame, text='Bottom label 2')
		self.label6 = tkinter.Label(self.top_frame, text='Bottom label 3')

		self.label4.pack(expand=True)
		self.label5.pack(expand=True)
		self.label6.pack(expand=True)

		self.top_frame.pack()

		self.bottom_frame.pack()

		tkinter.mainloop()

#def main():

#	gui_fool = MyGUI()

#main()