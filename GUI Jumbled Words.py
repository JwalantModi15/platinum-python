from tkinter import *
from tkinter import messagebox
import random

def correct():
    word = text.get()
    if word.upper() in answer:
        global c
        messagebox.showinfo("Win!", "Your answer is correct")
        ch = random.choice(words)
        text.set("")
        l1["text"] = ch
        c+=10
        count()
    else:
        messagebox.showinfo("Lose!", "Your answer is wrong")
        ch = random.choice(words)
        text.set("")
        l1["text"] = ch

def change():
    ch = random.choice(words)
    text.set("")
    l1["text"] = ch

def count():
    number.set(c)


root = Tk()
root.resizable(0,0)
root.geometry("400x350")
root.title("Jumble")
root.configure(bg = "lightblue")
answer = ["INDIA", "USA", "JAPAN", "FINLAND", "AUSTRALIA", "APPLE", "TIGER", "NEWDAY"]
words = ["AIDIN", "SUA", "NAJAP", "ANDLNFI", "SUTALAIRA", "PLEAP", "RTGEI", "YDEWAN"]
c = 0
ch = random.choice(words)

l = Label(root, text = "Your Word = ", font = ("", 12), fg = "black", bg = "lightblue")
l.place(x = 80, y = 45)
l1 = Label(root, text = ch, font = ("", 15), fg = "red", bg = "lightblue")
l1.place(x = 168, y = 41)

text = StringVar()
e1 = Entry(root, font = ("", 18), textvariable = text)
e1.focus_set()
e1.place(x = 65, y = 110)

number = IntVar()
l2 = Label(root, font = ("", 15), textvariable = number, bg = "lightblue")
l2.place(x = 5, y = 10)


b1 = Button(root, text = "Check", font = ("", 15), fg = "blue", command = correct)
b1.place(x = 155, y = 165)
b2 = Button(root, text = "Reset Word", font = ("", 15), command = change)
b2.place(x = 135, y = 235)
root.mainloop()