from tkinter import *
from random import *
from time import *

window = Tk()
window.geometry("1280x720")
window.title("Reaction Time Test")
window.config(bg="#1f2d38")
canvas = Canvas(window, width=1000, height=500, bg="#161f26")
canvas.pack(side=TOP, pady=3)

score = 0

global ms1
global ms2
global ls

def start():
    global ms1
    global ls

    ls = [click]
    x = randint(1, 900)
    y = randint(1, 400)
    s = canvas.create_oval(x, y, x+25, y+25, fill="red")#create square
    ms1 = int(round(time() * 1000))#convert time to millisecond
    canvas.tag_bind(s, '<ButtonPress-1>', choice(ls))#if square is clicked call function onClick

def click(event):
    global ms1
    global ms2
    global score
    global ls

    ls = [click]
    ms2 = int(round(time() * 1000))#get curnent time

    #+1 score if clicked on time
    if (ms2 - ms1) < 1500:
        print(ms2 - ms1,"Milliseconds")
        score += 1

    #fail to click on time
    if (ms2 - ms1) > 1500:
        print(ms2 - ms1, "Milliseconds")
        window.destroy()
        newWindow = Tk()
        newWindow.geometry("640x320")
        newWindow.title("Result")
        newWindow.config(bg="#1f2d38")


        score = Label(text="Final Score: %d" % score, fg = "WHITE", bg="#1f2d38", width=20, font='Bahnschrift 24 bold', pady = 20)
        result = Label(text="You were too slow", fg = "WHITE", bg="#1f2d38", width=100, font='Bahnschrift 50 bold', pady = 20)
        result.pack()
        score.pack()

        newWindow.mainloop()

    score_button.config(text="score: %d" % score)#update button for score
    canvas.delete('all')

    x = randint(1, 500)
    y = randint(1, 500)

    ms1 = int(round(time() * 1000))
    s = canvas.create_oval(x, y, x+25, y+25, fill="red")#create new square
    canvas.tag_bind(s, '<ButtonPress-1>', choice(ls))

    if score == 10:
        window.destroy()
        newWindow = Tk()
        newWindow.geometry("640x320")
        newWindow.title("Result")
        newWindow.config(bg="#1f2d38")


        score = Label(text="Final Score: %d" % score, fg = "WHITE", bg="#1f2d38", width=20, font='Bahnschrift 24 bold', pady = 20)
        result = Label(text="YOU WIN", fg = "WHITE", bg="#1f2d38", width=100, font='Bahnschrift 50 bold', pady = 20)
        result.pack()
        score.pack()

start_button = Button(window, text="START", command=start, bg="WHITE", bd=0, width=20, font='Bahnschrift 24 bold')
score_button = Label(text="score: %d" % score, bg="WHITE", width=20, font='Bahnschrift 24 bold')
score_button.pack()
start_button.pack()
window.mainloop()
