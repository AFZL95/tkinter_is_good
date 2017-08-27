#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk

# Create instance
win = tk.Tk()   

# Add a title       
win.title("Python Simple GUI")

# Modify adding a Label
aLabel = ttk.Label(win, text="")
aLabel.grid(column=0, row=0)

# Button Click Event Function
def clickMe():
    action.configure(text=" Name: " + name.get())

# Changing our Label
ttk.Label(win, text="Please Enter Your Full Name:").grid(column=0, row=0)

# Adding a Textbox Entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=20, textvariable=name)
nameEntered.grid(column=0, row=1)

# Adding a Button
action = ttk.Button(win, text="Click On Me Please!", command=clickMe)   
action.grid(column=1, row=1)
# this is used to disable functionality of a widget 
action.configure(state='enable')    # Disable the Button Widget

nameEntered.focus()      # Place cursor into name Entry
#======================
# Start GUI
#======================
win.mainloop()