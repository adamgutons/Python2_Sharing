from Tkinter import * 

root = Tk()

top = Toplevel()
top.geometry("500x500+100+100")				# We can position top level windows with Toplevel().  Hopefully this keeps a thread
											# in which we can show messages/display results from the robocopy success/failure
											# while the other window spins.  


top.title("TOP LEVEL")
root.title("MAIN WINDOW")
x  = Label(top, text="This goes here")

w  = Label(root, text="Hello adam")

w.pack()
x.pack()
root.mainloop()