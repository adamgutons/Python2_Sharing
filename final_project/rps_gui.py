import random
import tkinter

class make_rps():
	def __init__(self):
		#we need Toplevel b/c image paths get messed up when system sees multilple Tk() instances.  Toplevel() is like a frame
		#that appears
		self.main_window = tkinter.Toplevel() 
		self.rock_image = tkinter.PhotoImage(file='rock.gif')
		self.paper_image = tkinter.PhotoImage(file='paper.gif')		
		self.rps_title = tkinter.Label(self.main_window, bd=10, wraplength=300, text="ROCK PAPER SCISSORS: Yep, it's that simple..." )
		self.select_label = tkinter.Label(self.main_window)
		self.results_label = tkinter.Label(self.main_window, text='results')
		self.button1 = tkinter.Button(self.main_window, image=self.rock_image)
		self.button2 = tkinter.Button(self.main_window, image=self.paper_image)
		self.button3 = tkinter.Button(self.main_window, image=self.rock_image)
		self.quit_button = tkinter.Button(self.main_window, text='Quit', command=self.main_window.destroy)
		self.button1.bind('<Button-1>', self.rock_select)
		self.button2.bind('<Button-1>', self.paper_select)
		self.button3.bind('<Button-1>', self.scissors_select)
		self.rps_title.grid(columnspan=3)
		self.button1.grid(row=1, column=0, sticky='NSEW')
		self.button2.grid(row=1, column=1, sticky='NSEW')
		self.button3.grid(row=1, column=2, sticky='NSEW')
		self.results_label.grid(row=2, columnspan=3)
		self.select_label.grid(row=3, columnspan=3)
		self.quit_button.grid(row=4, columnspan=3, sticky='NSEW')
		tkinter.mainloop()

	def rock_select(self, event):
		self.results_label.config(text='Rock selected...')
		user_select = 'rock'
		self.play_game(user_select)

	def paper_select(self, event):
		self.results_label.config(text='Paper selected...')
		user_select = 'paper'
		self.play_game(user_select)

	def scissors_select(self, event):
		self.results_label.config(text='Scissors selected...')	
		user_select = 'scissors'
		self.play_game(user_select)
		 

	def play_game(self, user_select):
		#while start_game:
		#print('-' * 20)
		user_select = user_select
		comp_select = random.choice(['rock', 'paper', 'scissors'])
		a = "You win!"
		b = "Computer wins!"
		c = "Tie game..."
		self.select_label.config(text='User selects: %s\nComputer selects: %s' % (user_select, comp_select))
		print("Computer selects:", comp_select)
		if comp_select == user_select:
			readout = c
			self.results_label.config(text=readout)
		elif user_select == "rock": 
			if comp_select == "scissors":
				readout = a
				self.results_label.config(text=readout)
			else:
				readout = b
				self.results_label.config(text=readout)
		elif user_select == "paper": 
			if comp_select == "rock":
				readout = a
				self.results_label.config(text=readout)
			else:
				readout = b
				self.results_label.config(text=readout)
		elif user_select == "scissors": 
			if comp_select == "paper":
				readout = a
				self.results_label.config(text=readout)
			else:
				readout = b
				self.results_label.config(text=readout)
		else:
			self.results_label.config(text='Sorry something went wrong...')





