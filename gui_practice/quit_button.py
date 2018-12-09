import tkinter
import tkinter.messagebox
import frame_demo

class MyGUI():
	def __init__(self):
		
		self.main_window = tkinter.Tk()

		self.my_button = tkinter.Button(self.main_window, text='Click me!', command=self.do_something)
		self.quit_button = tkinter.Button(self.main_window, text='Quit', command=self.main_window.destroy)

		self.my_button.pack()
		self.quit_button.pack()

		tkinter.mainloop()

	def do_something(self):
		frame_goo = frame_demo.Frame_GUI()


def main():

	main_goo = MyGUI()

main()

		