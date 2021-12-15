import tkinter
window = tkinter.Tk()

window.title("Clicker")
window.config(bg="grey")
window.geometry("350x200")
count = 0
state = "neutral"

def f_add(event="none"):
    global state
    global count
    count += 1
    counter.configure(text = count)
    state = "up"

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

def f_subtract(event="none"):
    global state
    global count
    count -= 1
    counter.configure(text = count)
    state = "down"

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

def doubleClick(event):
    global count
    if state == "up":
        count *= 3
        counter.configure(text = count)
    elif state == "down":
        count //= 3
        counter.configure(text = count)
    else:
        pass



counter.bind("<Enter>", calc)
counter.bind("<Leave>", leave)
counter.bind("<Double-Button>", doubleClick)
window.bind("<Down>", f_subtract)
window.bind("-", f_subtract)
window.bind("<Up>", f_add)
window.bind("=", f_add)
window.bind("<space>", doubleClick)

window.mainloop()