#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# Create instance
win = tk.Tk()

# Add a title
win.title("Python GUI")

# Using a scrolled Text control
scrolW  = 30
scrolH  =  30
scr = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, columnspan=5)

#======================
# Start GUI
#======================
win.mainloop()
