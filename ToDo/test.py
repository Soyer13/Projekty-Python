'''
from tkinter import *
from tkcalendar import Calendar, DateEntry
#Create an instance of tkinter frame
win= Tk()
#Set the Geometry
win.geometry("750x250")
win.title("Date Picker")
#Create a Label
Label(win, text= "Choose a Date", background= 'gray61', foreground="white").pack(padx=20,pady=20)
#Create a Calendar using DateEntry
cal = DateEntry(win, width= 16, background= "magenta3", foreground= "white",bd=2)
cal.pack(pady=20)
win.mainloop()'''

# importing only those functions
# which are needed
from tkinter import *
from tkinter.ttk import *

# creating tkinter window
root = Tk()

# Adding widgets to the root window
Label(root, text='GeeksforGeeks', font=(
    'Verdana', 15)).pack(side=TOP, pady=10)

# Creating a photoimage object to use image
photo = PhotoImage(file="Update.png")

# here, image option is used to
# set image on button
Button(root, text='Click Me !', image=photo).pack(side=TOP)

mainloop()