from tkinter import *
from random import *
from time import *

score = 0
total = 0
count = 0

global ms1
global ms2
global ls
global speed
global difi


#class for win/loss
class WinLoss:
    #creates menu screen for "win"
    def win(self, average):
        clear_frame()

        final_score = Label(text="Final Score: %d" % self, fg="WHITE", bg="#1f2d38", width=20,
                            font='Bahnschrift 24 bold', pady=20)
        avg_time = Label(text="Average: %.2f Milliseconds" % average, fg="WHITE", bg="#1f2d38",
                         width=30, font='Bahnschrift 24 bold', pady=20)
        result = Label(text="YOU WIN", fg="WHITE", bg="#1f2d38", width=100, font='Bahnschrift 50 bold', pady=20)
        try_again = Button(window, text="RETURN", command=new_main, bg="WHITE", bd=0, width=20,
                           font='Bahnschrift 24 bold')

        result.pack()
        final_score.pack()
        avg_time.pack()
        try_again.pack()

    # creates menu screen for "loss"
    def loss(self):
        global score
        score = 0
        clear_frame()

        final_score = Label(text="Final Score: %d" % self, fg="WHITE", bg="#1f2d38", width=20,
                            font='Bahnschrift 24 bold', pady=20)
        result = Label(text="You were too slow!\nTry again", fg="WHITE", bg="#1f2d38", width=100,
                       font='Bahnschrift 50 bold', pady=20)
        try_again = Button(window, text="RETURN", command=new_main, bg="WHITE", bd=0, width=20,
                           font='Bahnschrift 24 bold')
        result.pack()
        final_score.pack()
        try_again.pack()


#class for different difficulties
class Difficulty:
    def easy(self):
        global speed
        speed = 2000
        return speed

    def normal(self):
        global speed
        speed = 1500
        return speed

    def hard(self):
        global speed
        speed = 1000
        return speed


Difficulty.normal(10)


def clear_frame():
    for widget in window.winfo_children():
        widget.destroy()


#function for start of game
def start():
    global ms1
    global ls
    ls = [on_click]
    x = randint(1, 900)
    y = randint(1, 400)

    create_oval = canvas.create_oval(x, y, x+25, y+25, fill="red")  #create circle
    ms1 = int(round(time() * 1000))  #convert time to millisecond
    canvas.tag_bind(create_oval, '<ButtonPress-1>', choice(ls))  #if square is clicked call function click


def on_click(event):
    global ms1
    global ms2
    global score
    global ls
    global count
    global total

    ls = [on_click]

    # get time
    ms2 = int(round(time() * 1000))

    #+1 score if clicked on time
    if (ms2 - ms1) < speed:
        print(ms2 - ms1, "Milliseconds")
        score += 1

    #fail to click on time
    if (ms2 - ms1) > speed:
        WinLoss.loss(score)

    #get average
    total += ms2 - ms1
    count += 1
    average = total / count

    # update button for score
    score_button.config(text="score: %d" % score)
    canvas.delete('all')

    x = randint(1, 500)
    y = randint(1, 500)

    #get new time
    ms1 = int(round(time() * 1000))

    # create new circle
    s = canvas.create_oval(x, y, x+25, y+25, fill="red")
    canvas.tag_bind(s, '<ButtonPress-1>', choice(ls))

    #execute "win" screen
    if score == 10:
        print("Average: ", average, "Milliseconds")
        WinLoss.win(score, average)
        score = 0


#create ui for return
def new_main():
    global canvas
    global start_button
    global score_button
    global settings

    clear_frame()

    canvas = Canvas(window, width=1000, height=500, bg="#161f26")
    score_button = Label(text="score: %d" % score, bg="WHITE", width=20, font='Bahnschrift 24 bold')
    start_button = Button(window, text="START", command=start, bg="WHITE", bd=0, width=20, font='Bahnschrift 24 bold')
    settings = Button(window, text="SETTINGS", command=options, bg="WHITE", bd=1, width=15, font='Bahnschrift 24 bold')
    canvas.pack(side=TOP, pady=3)
    score_button.pack()
    start_button.pack()
    settings.pack(pady=2)


#ui for options tab
def options():
    clear_frame()

    title = Label(text="SETTINGS", bg="#1f2d38", bd=0, width=30, font='Bahnschrift 64 bold')
    difficulty = Label(text="difficulty:", bg="WHITE", width=20, font='Bahnschrift 24 bold')
    easy = Button(window, text="EASY(2 sec)", command=Difficulty.easy(10), bg="WHITE", bd=0, width=20,
                  font='Bahnschrift 24 bold', activebackground='red')
    normal = Button(window, text="NORMAL(1.5 sec)", command=Difficulty.normal(10), bg="WHITE",
                    bd=0, width=20, font='Bahnschrift 24 bold', activebackground='red')
    hard = Button(window, text="HARD(1 sec)", command=Difficulty.hard(10), bg="WHITE", bd=0, width=20,
                  font='Bahnschrift 24 bold', activebackground='red')
    try_again = Button(window, text="RETURN", command=new_main, bg="WHITE", bd=0, width=20,
                       font='Bahnschrift 24 bold')
    title.pack(pady=5)
    difficulty.pack(pady=5)
    easy.pack(pady=5)
    normal.pack(pady=5)
    hard.pack(pady=5)
    try_again.pack(pady=5)


window = Tk()
window.geometry("1280x720")
window.title("Reaction Time Test")
window.config(bg="#1f2d38")
canvas = Canvas(window, width=1000, height=500, bg="#161f26")
score_button = Label(text="score: %d" % score, bg="WHITE", width=20, font='Bahnschrift 24 bold')
start_button = Button(window, text="START", command=start, bg="WHITE", bd=0, width=20, font='Bahnschrift 24 bold')
settings = Button(window, text="SETTINGS", command=options, bg="WHITE", bd=1, width=15, font='Bahnschrift 24 bold')
canvas.pack(side=TOP, pady=3)
score_button.pack()
start_button.pack()
settings.pack(pady=2)
window.mainloop()
