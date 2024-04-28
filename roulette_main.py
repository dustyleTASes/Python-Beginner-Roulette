#define
def checkLost():
    randnum = rd.randint(1,2)

    if randnum == 1:
        rmsg.set("Alive")
    elif randnum == 2:
        exit()

#imports
import tkinter as tk
import random as rd

#window variable
win = tk.Tk()

#window setuup
win.geometry("250x150")
win.title("Python Roulette")

#roulette message
rmsg = tk.StringVar()

#pack in window
rlabel = tk.Label(win, text="Press to shoot!\nIf you lose you will exit in an instant.")
rlabel.pack()

sbutton = tk.Button(win, text="Shoot!", command=checkLost)
sbutton.pack()

lblrmsg = tk.Label(win, fg="black", textvariable=rmsg)
lblrmsg.pack()

#window update
win.mainloop()
