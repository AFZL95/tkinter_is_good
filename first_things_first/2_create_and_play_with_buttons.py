#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk

# Create instance
win = tk.Tk()   

# Add a title       
win.title("Python Simple GUI")

# Disable resizing the GUI
# win.resizable(0,2)    

# Modify adding a Label
aLabel = ttk.Label(win, text="Hello, I am a useless Label")
aLabel.grid(column=0, row=0)

# Button Click Event Function
def clickMe():
    action.configure(text=" I have been Clicked! ")
    aLabel.configure(foreground='red')
    aLabel.configure(text="Wooow! I'm changed now!")

# Adding a Button
action = ttk.Button(win, text="Click on Me Please!", command=clickMe)   
action.grid(column=0, row=1)


#======================
# Fire Up GUI
#======================
win.mainloop()