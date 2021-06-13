from tkinter import *
from tkinter.ttk import *

window=Tk()

# Radio button widget
v0=IntVar()
v0.set(1)
r1=Radiobutton(window, text="This", variable=v0, value=1)
r2=Radiobutton(window, text="Or that", variable=v0, value=2)
r1.place(x=100,y=50)
r2.place(x=180, y=50)


# Check button widget                
v1 = IntVar()
v2 = IntVar()
c1 = Checkbutton(window, text="This", variable=v1)
c2 = Checkbutton(window, text="And that", variable=v2)
c1.place(x=100, y=100)
c2.place(x=180, y=100)


# Combobox widget
var = StringVar()
var.set("one")
data = ("Texas", "Oklahoma", "Louisiana", "Arkansas")
cb = Combobox(window, values=data)
cb.place(x=100, y=150)


# Listbox widget
lb = Listbox(window, height=5, selectmode='multiple')
for num in data:
    lb.insert(END, num)
lb.place(x=100, y=200)


# Slider widget
v3 = IntVar()
s1 = Scale(window, orient=HORIZONTAL, variable=v3)
s1.place(x=100, y=300)
s1_label = Label(window, textvariable="")
s1_label.place(x=200, y=300)

window.title('Main Window')
window.geometry("1600x800+20+40")
window.mainloop()
