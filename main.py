from tkinter import *
import random

top = Tk()
top.geometry("350x350")
top.title("Rock Paper Scissor ")
top.config(bg="blue")

computer_score = {"0": "Rock", "1": "Paper", "2": "Scissor"}


def resetthegame():
    b1["state"] = "active"

    b2["state"] = "active"

    b3["state"] = "active"

    l1.config(text="You              ")

    l3.config(text="Computer")

    l4.config(text="")


# Disable the Button

def disablethebutton():
    b1["state"] = "disable"

    b2["state"] = "disable"

    b3["state"] = "disable"


# If player selected rock

def isrock():
    c_s = computer_score[str(random.randint(0, 2))]

    if c_s == "Rock":

        match_result = "Match Draw"

    elif c_s == "Scissor":

        match_result = "You Win"

    else:

        match_result = "Computer Win"

    l4.config(text=match_result)

    l1.config(text="Rock            ")

    l3.config(text=c_s)

    disablethebutton()


def ispaper():  # If player selected paper
    c_s = computer_score[str(random.randint(0, 2))]

    if c_s == "Paper":

        match_result = "Match Draw"

    elif c_s == "Scissor":

        match_result = "Computer Win"

    else:

        match_result = "You Win"

    l4.config(text=match_result)

    l1.config(text="Paper           ")

    l3.config(text=c_s)

    disablethebutton()


def isscissor():            # If player selected scissor
    c_s = computer_score[str(random.randint(0, 2))]

    if c_s == "Rock":

        match_result = "Computer Win"

    elif c_s == "Scissor":

        match_result = "Match Draw"

    else:

        match_result = "You Win"

    l4.config(text=match_result)

    l1.config(text="Scissor         ")

    l3.config(text=c_s)

    disablethebutton()


# Add Labels, Frames and Button
Label(top, text="Rock Paper Scissor", font="arial 20 bold", fg="red").pack(pady=20)

frame = Frame(top)
frame.pack()

l1 = Label(frame, text="YOU              ", font=10)

l2 = Label(frame, text="VS             ", font="arial 10 bold")

l3 = Label(frame, text="COMPUTER", font=10)

l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()

l4 = Label(top, text="", font="arial 20 bold", bg="green", width=15)

l4.pack(pady=20)

frame1 = Frame(top)
frame1.pack()

b1 = Button(frame1, text="Rock", font=10, height=8, width=8, bg="orange", command=isrock)

b2 = Button(frame1, text="Paper ", font=10, height=8, width=8, bg="orange", command=ispaper)

b3 = Button(frame1, text="Scissor", font=10, height=8, width=8, bg="orange", command=isscissor)

b1.pack(side=LEFT, padx=10)

b2.pack(side=LEFT, padx=10)

b3.pack(padx=10)
canvas= Canvas(height=2,width=1,bg="white")
canvas.pack()
photo1= PhotoImage(file="C:\\Users\\riyac\\Documents\\GAME.png")
canvas.create_image(20,20,image=photo1,anchor=CENTER)
l5=Label(top, image=photo1).pack(side=LEFT,padx=10)


Button(top, text="Reset Game", font=10, fg="black", bg="red", command=resetthegame).pack(pady=20)

# Execute Tkinter
top.mainloop()
