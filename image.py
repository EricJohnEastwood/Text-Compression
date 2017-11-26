from tkinter import *
from tkinter import messagebox
import os

# The GUI part

# this calls the help menu
def help1():
    label = messagebox.showinfo("Help","""Enter command\n
    	1: Extracting the text\n
    	2: Compressing the text\n
    	3: Quit\nFile name should be given with extension\n
    	""")


# this calls the main.py
def execute():
    exec(open("main.py").read())

# remaining works on visual and screen
root = Tk()
root.title("Data compression")


frame = Frame(root,height = 450,width = 1500)
c = Canvas(root,height = 450,width = 1500)

filename = PhotoImage(file = "pr.gif")

background_label = Label(root,image = filename)
background_label.place(x=0,y=0)


photo = PhotoImage(file = "index1.gif")

label = Label(root,image = photo)
label.pack()


button1 = Button(root,text = "RUN",fg = "black",bg = "white",command = execute,height = 0,width = 6)
button2 = Button(root,text = "HELP",fg = "black",bg = "white",command =help1,height = 0,width = 6)

button1.pack(side = BOTTOM)
button2.pack(side =BOTTOM)

c.pack()
frame.pack()



root.mainloop()

