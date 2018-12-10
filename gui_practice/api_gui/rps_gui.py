import random
import tkinter

class make_rps():
	def __init__(self):
		#we need Toplevel b/c image paths get messed up when system sees multilple Tk() instances.  Toplevel() is like a frame
		#that appears
		self.main_window = tkinter.Toplevel() 
		self.rock_image = tkinter.PhotoImage(file='rock.gif')
		self.rps_title = tkinter.Label(self.main_window, wraplength=300, text="ROCK PAPER SCISSORS: Yep, it's that simple...results are written to a file..." )
		self.results_label = tkinter.Label(self.main_window, text='results')
		self.button = tkinter.Button(self.main_window, image=self.rock_image)
		self.button2 = tkinter.Button(self.main_window, image=self.rock_image)
		self.button3 = tkinter.Button(self.main_window, image=self.rock_image)
		self.rps_title.grid(columnspan=3)
		self.button.grid(row=1, column=0, sticky='NSEW')
		self.button2.grid(row=1, column=1, sticky='NSEW')
		self.button3.grid(row=1, column=2, sticky='NSEW')
		self.results_label.grid(columnspan=3)
		tkinter.mainloop()

	def play_game(game_counter, start_game, dat_file):
		while start_game:
			print('-' * 20)
			user_select = input("Type 'rock', 'paper', 'scissors' to play, 'quit' to quit >> ")
			comp_select = random.choice(['rock', 'paper', 'scissors'])
			game_counter += 1
			if user_select == 'quit':
				start_game = False
				dat_file.close()
			else:
				a = "You win!"
				b = "Computer wins!"
				c = "Tie game..."
				print('-' * 20)
				print("User selects:", user_select)
				print("Computer selects:", comp_select)
				if comp_select == user_select:
					readout = "Game " + str(game_counter) + " " + c
					print(str(readout))
					dat_file.write(str(readout) + '\n')
				elif user_select == "rock": 
					if comp_select == "scissors":
						readout = "Game " + str(game_counter) + " " + a
						print(str(readout))
						dat_file.write(str(readout) + '\n')
					else:
						readout = "Game " + str(game_counter) + " " + b
						print(str(readout))
						dat_file.write(str(readout) + '\n')	
				elif user_select == "paper": 
					if comp_select == "rock":
						readout = "Game " + str(game_counter) + " " + a
						print(str(readout))
						dat_file.write(str(readout) + '\n')
					else:
						readout = "Game " + str(game_counter) + " " + b
						print(str(readout))
						dat_file.write(str(readout) + '\n')
				elif user_select == "scissors": 
					if comp_select == "paper":
						readout = "Game " + str(game_counter) + " " + a
						print(str(readout))
						dat_file.write(str(readout) + '\n')
					else:
						readout = "Game " + str(game_counter) + " " + b
						print(str(readout))
						dat_file.write(str(readout) + '\n')
				else:
					print("Invalid user entry, try again...")





