#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as mBox

# Create instance
win = tk.Tk()

# Add a title
win.title("Python GUI")

# We are creating a container frame to hold all other widgets
my_first_frame = ttk.LabelFrame(win, text="FZL's Frame")
my_first_frame.grid(column=0, row=0, padx=8, pady=4)

# Modified Button Click Function
def clickMe():
    action.configure(text='Hello ' + name.get())

# Changing our Label
ttk.Label(my_first_frame, text="Enter a name:").grid(column=0, row=0, sticky='W')

# Adding a Textbox Entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(my_first_frame, width=12, textvariable=name)
nameEntered.grid(column=0, row=1, sticky='W')

# Adding a Button
action = ttk.Button(my_first_frame, text="Click Me!", command=clickMe)
action.grid(column=2, row=1)

ttk.Label(my_first_frame, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
numberChosen = ttk.Combobox(my_first_frame, width=12, textvariable=number)
numberChosen['values'] = (1, 2, 4, 42, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)

# Creating three checkbuttons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(my_first_frame, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W, columnspan=3)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(my_first_frame, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W, columnspan=3)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(my_first_frame, text="Toggle", variable=chVarEn)
check3.deselect()
check3.grid(column=2, row=4, sticky=tk.W, columnspan=3)

# GUI Callback function
def checkCallback(*ignoredArgs):
    # only enable one checkbutton
    if chVarUn.get(): check3.configure(state='disabled')
    else:             check3.configure(state='normal')
    if chVarEn.get(): check2.configure(state='disabled')
    else:             check2.configure(state='normal')

# trace the state of the two checkbuttons
chVarUn.trace('w', lambda unused0, unused1, unused2 : checkCallback())
chVarEn.trace('w', lambda unused0, unused1, unused2 : checkCallback())

# Using a scrolled Text control
scrolW  = 30; scrolH  =  3
scr = scrolledtext.ScrolledText(my_first_frame, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, sticky='WE', columnspan=3)

# Radiobutton list
colors = ["Blue", "Gold", "Red"]

# Radiobutton callback function
def radCall():
    radSel=radVar.get()
    if   radSel == 0: win.configure(background=colors[0])
    elif radSel == 1: win.configure(background=colors[1])
    elif radSel == 2: win.configure(background=colors[2])

radVar = tk.IntVar()

# Selecting a non-existing index value for radVar
radVar.set(99)

# Creating all three Radiobutton widgets within one loop
for col in range(3):
    curRad = 'rad' + str(col)
    curRad = tk.Radiobutton(my_first_frame, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=6, sticky=tk.W, columnspan=3)

# Create a container to hold labels
labelsFrame = ttk.LabelFrame(my_first_frame, text=' Labels in a Frame ')
labelsFrame.grid(column=0, row=7)

# Place labels into the container element - vertically
ttk.Label(labelsFrame, text="Label1").grid(column=0, row=0)
ttk.Label(labelsFrame, text="Label2").grid(column=0, row=1)
ttk.Label(labelsFrame, text="Label3").grid(column=0, row=2)

# Add some space around each label
for child in labelsFrame.winfo_children():
    child.grid_configure(padx=8, pady=1)

    # Display a Message Box
    def _msgBox():
        answer = mBox.askyesno("to be or not to be, that's the question", "Are you sure you really want to quit?")
        print(answer)
        if answer == True:
            _quit()

# Exit GUI cleanly
def _quit():
    win.quit()
    win.destroy()
    exit()

# Creating a Menu Bar
menuBar = Menu(win)
win.config(menu=menuBar)

# Add menu items
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_msgBox)
menuBar.add_cascade(label="File", menu=fileMenu)


# Add another Menu to the Menu Bar and an item
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help", menu=helpMenu)


# Place cursor into name Entry
nameEntered.focus()
#======================
# Start GUI
#======================
win.mainloop()
