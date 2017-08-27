#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import Spinbox


class ToolTip(object):
    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, _cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 27
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))

        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                      background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                      font=("tahoma", "12", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

#===================================================================
def createToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)

# Create instance
win = tk.Tk()

# Add a title
win.title("Python GUI")

# Tab Control introduced here --------------------------------------
tabControl = ttk.Notebook(win)          # Create Tab Control

tab1 = ttk.Frame(tabControl)            # Create a tab
tabControl.add(tab1, text='First tab')      # Add the tab

tab2 = ttk.Frame(tabControl)            # Add a second tab
tabControl.add(tab2, text='Second tab')      # Make second tab visible

tab3 = ttk.Frame(tabControl)            # Add a third tab
tabControl.add(tab3, text='Third tab')      # Make second tab visible

tabControl.pack(expand=1, fill="both")  # Pack to make visible
# ~ Tab Control introduced here -----------------------------------------

# We are creating a container tab3 to hold all other widgets
my_first_frame = ttk.LabelFrame(tab1, text="FZL's Frame")
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
# Add a Tooltip
createToolTip(nameEntered, 'Enter your full name')

# Adding a Button
action = ttk.Button(my_first_frame, text="Click Me!", command=clickMe)
action.grid(column=2, row=1)

ttk.Label(my_first_frame, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
numberChosen = ttk.Combobox(my_first_frame, width=12, textvariable=number)
numberChosen['values'] = (1, 2, 4, 42, 100)
numberChosen.grid(column=1, row=1)
numberChosen.current(0)

# Spinbox callback
def _spin():
    value = spin.get()
    print(value)
    scr.insert(tk.INSERT, value + '\n')

# Adding a Spinbox widget using a set of values
spin = Spinbox(my_first_frame, values=(1, 2, 4, 42, 100), width=5, bd=8, command=_spin)
spin.grid(column=0, row=2)

# Add a Tooltip
createToolTip(spin, 'This is a Spin control.')


# Using a scrolled Text control
scrolW  = 30; scrolH  =  3
scr = scrolledtext.ScrolledText(my_first_frame, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, row=3, sticky='WE', columnspan=3)

# Tab Control 2 refactoring  -----------------------------------------
# We are creating a container tab3 to hold all other widgets -- Tab2
my_second_frame = ttk.LabelFrame(tab2, text=' The Snake ')
my_second_frame.grid(column=0, row=0, padx=8, pady=4)
# Creating three checkbuttons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(my_second_frame, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=0, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(my_second_frame, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=0, sticky=tk.W )

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(my_second_frame, text="Toggle", variable=chVarEn)
check3.deselect()
check3.grid(column=2, row=0, sticky=tk.W)

# GUI Callback function
def checkCallback(*ignoredArgs):
#     only enable one checkbutton
    if chVarUn.get(): check3.configure(state='disabled')
    else:             check3.configure(state='normal')
    if chVarEn.get(): check2.configure(state='disabled')
    else:             check2.configure(state='normal')

# trace the state of the two checkbuttons
chVarUn.trace('w', lambda unused0, unused1, unused2 : checkCallback())
chVarEn.trace('w', lambda unused0, unused1, unused2 : checkCallback())
# ~ Tab Control 2 refactoring  -----------------------------------------

# Radiobutton list
colors = ["Blue", "Gold", "Red"]

# Radiobutton callback function
def radCall():
    radSel=radVar.get()
    if   radSel == 0: my_second_frame.configure(text='Blue')
    elif radSel == 1: my_second_frame.configure(text='Gold')
    elif radSel == 2: my_second_frame.configure(text='Red')

radVar = tk.IntVar()

# Selecting a non-existing index value for radVar
radVar.set(99)

# Creating all three Radiobutton widgets within one loop
for col in range(3):
    curRad = 'rad' + str(col)
    curRad = tk.Radiobutton(my_second_frame, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=6, sticky=tk.W, columnspan=3)

# Create a container to hold labels
labelsFrame = ttk.LabelFrame(my_second_frame, text=' Labels in a Frame ')
labelsFrame.grid(column=0, row=7)

# Place labels into the container element - vertically
ttk.Label(labelsFrame, text="Label1").grid(column=0, row=0)
ttk.Label(labelsFrame, text="Label2").grid(column=0, row=1)

# Add some space around each label
for child in labelsFrame.winfo_children():
    child.grid_configure(padx=8)

# Exit GUI cleanly
def _quit():
    win.quit()
    win.destroy()
    exit()

# Tab Control 3 -------------------------------
tab3 = tk.Frame(tab3, bg='blue')
tab3.pack()
for orangeColor in range(2):
    canvas = tk.Canvas(tab3, width=150, height=80, highlightthickness=0, bg='orange')
    canvas.grid(row=orangeColor, column=orangeColor)

# Creating a Menu Bar
menuBar = Menu(tab1)
win.config(menu=menuBar)

# Add menu items
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=_quit)
menuBar.add_cascade(label="File", menu=fileMenu)

# Add another Menu to the Menu Bar and an item
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About")
menuBar.add_cascade(label="Help", menu=helpMenu)

# Change the main windows icon
#win.iconbitmap(r'C:\Python34\DLLs\pyc.ico')

# Place cursor into name Entry
nameEntered.focus()
#======================
# Start GUI
#======================
win.mainloop()
