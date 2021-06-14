from tkinter import *
from tkinter import ttk
import matplotlib as mpl

mpl.use()


root = Tk()
root.title("Tkinter experiments")
# root.geometry("1600x800+20+40")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

childframe = ttk.Frame(mainframe, padding="3 3 12 12")
childframe.grid(row=1, column=3, sticky=(N, W, E, S))
# childframe['borderwidth'] = 2
# childframe['relief'] = 'sunken'

style = ttk.Style()
style.configure('Danger.TFrame', background='red', borderwidth=5, relief='raised')
ttk.Frame(childframe, width=200, height=200, style='Danger.TFrame').grid()

# Radio button widget
v0 = IntVar()
v0.set(1)
rb1 = ttk.Radiobutton(mainframe, text="This", variable=v0, value=1)
rb2 = ttk.Radiobutton(mainframe, text="Or that", variable=v0, value=2)
rb1.grid(row=1, column=1, sticky=(W, E))
rb2.grid(row=1, column=2, sticky=(W, E))

# Check button widget
v1 = IntVar()
v2 = IntVar()
ch1 = ttk.Checkbutton(mainframe, text="This", variable=v1)
ch2 = ttk.Checkbutton(mainframe, text="And that", variable=v2)
ch1.grid(row=2, column=1, sticky=(W, E))
ch2.grid(row=2, column=2, sticky=(W, E))

# Combobox widget
var = StringVar()
var.set("one")
data = ("Texas", "Oklahoma", "Louisiana", "Arkansas")
cb = ttk.Combobox(mainframe, values=data)
cb.grid(row=3, column=1, sticky=(W, E))

# Listbox widget
lb = Listbox(mainframe, height=5, selectmode='multiple')
for num in data:
    lb.insert(END, num)
lb.grid(row=4, column=1, sticky=(W, E))


# Scale widget
scale_label = ttk.Label(mainframe, text='0')
scale_label.grid(row=5, column=2, sticky=(W, E))

def update_label(scale_value):
    scale_label['text'] = scale_value

scale_value = StringVar()
scale = ttk.Scale(mainframe, orient=HORIZONTAL, from_=-90, to=90, variable=scale_value, command=update_label)
scale.set(0)
scale.grid(row=5, column=1, sticky=(W, E))


## Labeled Scale
# ttk.LabeledScale()
# labScale_value = StringVar()
# labScale = ttk.LabeledScale(master=mainframe, variable=labScale_value, from_=-90, to=90)
# labScale.label.lift()
# labScale.grid(row=6, column=1, sticky=(W, E))

for child in mainframe.winfo_children():
    child.grid_configure(padx=10, pady=10)
rb1.focus()

frame_label = ttk.Label(childframe, text="Child frame")
frame_label.grid(row=1, column=3, sticky=(W, E))

for child in childframe.winfo_children():
    child.grid_configure(padx=10, pady=10)

root.mainloop()
