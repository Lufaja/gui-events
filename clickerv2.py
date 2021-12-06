import tkinter
from tkinter.constants import Y
window = tkinter.Tk()

window.title("Clicker")
window.config(bg="grey")
window.geometry("350x200")
count = 0


def f_add():
    global count
    count += 1
    counter.configure(text = count)

#button to add to count
add = tkinter.Button(
    window,
    text="Up",
    width=25,
    height=1,
    command= f_add
)
add.pack()
add.place(anchor="center", x=175, y=50)

def f_subtract():
    global count
    count -= 1
    counter.configure(text = count)

#button to lower count
subtract = tkinter.Button(
    window,
    text="Down",
    width=25,
    height=1,
    command=f_subtract
)
subtract.pack()
subtract.place(anchor="center", x=175, y=150)

#shows current count
counter = tkinter.Label(
    window,
    height=1,
    width=25,
    text=count
)
counter.pack()
counter.place(anchor="center", x=175, y=100)

def calc(event):
    if count > 0:
        window.config(bg = "green")
    elif count < 0 :
        window.config(bg= "red")
    else:
        window.config(bg= "grey")

def leave(event):
    window.config(bg="grey")

counter.bind("<Enter>", calc)
counter.bind("<Leave>", leave)

window.mainloop()