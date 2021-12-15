import threading
import tkinter

window = tkinter.Tk()
btn = tkinter.Button(window)
btn.pack()
print(threading.active_count())
btn.bind("<space>")
print(threading.active_count())
window.mainloop()
print(threading.active_count())