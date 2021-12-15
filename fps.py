import tkinter
import time
import threading
import random
import sys

window = tkinter.Tk()
window.title("FPS Trainer")
window.geometry("500x350")
window.config(bg="black")

list = ["Press W", "Press A", "Press D", "Press S", "Press Space", "Single Click", "Double Click", "Triple Click"]
popUp = 0
t = 20
score = 0
pointVar = tkinter.StringVar()
pointVar = str(score) + " Point(s)"
exit_event = threading.Event()

def reset():
    global t, score, exit_event, start, popUp, start
    popUp.destroy()
    exit_event.clear()
    t = 20
    score = 0
    pointVar = str(score) + " Point(s)"
    points.config(text=pointVar)
    currentTime = ("time: " + str(t))
    timer.config(text=currentTime)
    start = tkinter.Button(
        window,
        text="Start",
        command=f_start
    )
    start.pack()
    start.place(anchor="c", x=250, y=175)





currentTime = ("time: " + str(t))

def popup():
    global popUp
    popUp = tkinter.Tk()
    popUp.geometry("200x200")
    retry = tkinter.Button(
        popUp,
        text = "Retry",
        width= 3,
        height= 1,
        command=reset
    )
    retry.pack()
    retry.place(anchor= "s", x= 50, y=150)
    def stop():
        popUp.destroy()
        window.destroy()
    quit = tkinter.Button(
        popUp,
        text = "Quit",
        width = 3,
        height= 1,
        command=stop
    )
    pointVar = str(score) + " Point(s)"
    label1 = tkinter.Label(
    popUp,
    text = pointVar
    )
    label1.pack()
    label1.place(anchor="c", x = "100", y = "75")
    quit.pack()
    quit.place(anchor= "s", x= 150, y=150)
    popUp.mainloop()

def bindVar(var):
    if var == "Press W":
        return "w"
    elif var == "Press A":
        return "a"
    elif var == "Press D":
        return "d"
    elif var == "Press S":
        return "s"
    elif var == "Press Space":
        return "<space>"
    elif var == "Single Click":
        return "<Button-1>"
    elif var == "Double Click":
        return "<Double-Button-1>"
    elif var == "Triple Click":
        return "<Triple-Button-1>"

def f_randomLabel():
    if t == 0:
        popup()
    else:    
        global pointVar
        randBind = random.choice(list)
        var1 = bindVar(randBind)
        randomLabel = tkinter.Label(
            window,
            text=randBind,
            width=10,
            height=2
        )
        randomLabel.pack()
        randomLabel.place(x=(random.randint(0,421)), y=random.randint(36, 307))
        def hit(event):
            global score
            global exit_event
            if "Press" in randBind:
                score += 1
            else:
                score += 2
            randomLabel.destroy()
            exit_event.set()
            if "Press" in randBind:
                window.unbind(var1)
            pointVar = (str(score) + " Point(s)")
            points.config(text=pointVar)
            f_randomLabel()
        if "Press" in randBind:
            window.bind(var1, hit)
        else:
            randomLabel.bind(var1, hit)
        def help():
            if exit_event.wait(timeout=2):
                exit_event.clear()
                if t == 0:
                    randomLabel.destroy()
                    popup()
                pass
            else:
                randomLabel.destroy()
                if "Press" in randBind:
                    window.unbind(var1)
                f_randomLabel()
        def help_thread():
            helpA = threading.Thread(target=help)
            helpA.daemon = True
            helpA.start()
        help_thread()




def countdown():
    global t
    global currentTime
    while t != 0 :
        time.sleep(1)
        t -= 1
        currentTime = ("time: " + str(t))
        timer.config(text=currentTime)
    exit_event.set()


def f_timer():
    countdown_thread = threading.Thread(target = countdown)
    countdown_thread.daemon = True
    countdown_thread.start()
 
timer = tkinter.Label(
    window,
    text = currentTime,
    padx=125
)

timer.pack()
timer.place(anchor="n", x=125)

points = tkinter.Label(
    window,
    text=pointVar,
    padx=125
)

points.pack()
points.place(anchor="n", x=375)


def f_start():
    start.destroy()
    f_timer()
    f_randomLabel()


start = tkinter.Button(
    window,
    text="Start",
    command=f_start
)
start.pack()
start.place(anchor="c", x=250, y=175)
window.mainloop()
sys.exit()