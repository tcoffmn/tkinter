from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Tkinter experiments")
#root.geometry("1600x800+20+40")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Radio button widget
v0 = IntVar()
v0.set(1)
r1 = ttk.Radiobutton(mainframe, text="This", variable=v0, value=1)
r2 = ttk.Radiobutton(mainframe, text="Or that", variable=v0, value=2)
r1.grid(row=1, column=1, sticky=(W, E))
r2.grid(row=1, column=2, sticky=(W, E))


# Check button widget
v1 = IntVar()
v2 = IntVar()
c1 = ttk.Checkbutton(mainframe, text="This", variable=v1)
c2 = ttk.Checkbutton(mainframe, text="And that", variable=v2)
c1.grid(row=2, column=1, sticky=(W, E))
c2.grid(row=2, column=2, sticky=(W, E))


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
v3 = IntVar()
s1 = ttk.Scale(mainframe, orient=HORIZONTAL, variable=v3)
s1.grid(row=5, column=1, sticky=(W, E))

s1_label = Label(mainframe, text="Label")
#s1_label = Label(mainframe, textvariable="")
s1_label.grid(row=5, column=2, sticky=(W, E))

for child in mainframe.winfo_children():
    child.grid_configure(padx=10, pady=10)
r1.focus()
#root.bind("<Return>", calculate)

root.mainloop()
