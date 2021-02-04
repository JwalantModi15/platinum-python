from tkinter import *
import random
from tkinter import messagebox

def text_onButton(button):
    global choosen_list
    choosen = random.choice(l)
    choosen_list.append(choosen)
    if choosen == "bomb" and button["text"]=="":
        button.config(text = choosen, bg = "red", fg = "white")
        messagebox.showinfo("Lose!", "It's a Bomb")
        main()
    elif button["text"]=="":    
        button.config(text = choosen)
        winner()

def winner():
    if "bomb" not in choosen_list and len(choosen_list)==25:
        messagebox.showinfo("Win!", "You Wins")
        main()

root = Tk()
root.geometry("488x430")
choosen_list = []
l = ["1","2","3","4","5","bomb","7","8","9","10","11","12","13","bomb","15","16","17","18","19","20","21","bomb","23","24","25"]
random.shuffle(l)

def main():
    b1 = Button(root, text = "", font = ("", 15), width = 8, height = 3, command = lambda: text_onButton(b1))
    b1.grid(row = 0, column = 0)
    b2 = Button(root, text = "", font = ("", 15), width = 8, height = 3, command = lambda: text_onButton(b2))
    b2.grid(row = 0, column = 1)
    b3 = Button(root, text = "", font = ("", 15), width = 8, height = 3, command = lambda: text_onButton(b3))
    b3.grid(row = 0, column = 2)
    b4 = Button(root, text = "", font = ("", 15), width = 8, height = 3, command = lambda: text_onButton(b4))
    b4.grid(row = 0, column = 3)
    b5 = Button(root, text = "", font = ("", 15), width = 8, height = 3, command = lambda: text_onButton(b5))
    b5.grid(row = 0, column = 4)

    b6 = Button(root, text = "", font = ("", 15), width = 8, height = 3, command = lambda: text_onButton(b6))
    b6.grid(row = 1, column = 0)
    b7 = Button(root, text = "", font = ("", 15), width = 8, height = 3, command = lambda: text_onButton(b7))
    b7.grid(row = 1, column = 1)
    b8 = Button(root, text = "", font = ("", 15), width = 8, height = 3, command = lambda: text_onButton(b8))
    b8.grid(row = 1, column = 2)
    b9 = Button(root, text = "", font = ("", 15), width = 8, height = 3, command = lambda: text_onButton(b9))
    b9.grid(row = 1, column = 3)
    b10 = Button(root, text = "", font = ("", 15), width = 8, height = 3, command = lambda: text_onButton(b10))
    b10.grid(row = 1, column = 4)

    b11 = Button(root, text = "", font = ("", 15), width = 8, height = 3, command = lambda: text_onButton(b11))
    b11.grid(row = 2, column = 0)
    b12 = Button(root, text = "", font = ("", 15), width = 8, height = 3, command = lambda: text_onButton(b12))
    b12.grid(row = 2, column = 1)
    b13 = Button(root, text = "", font = ("", 15), width = 8, height = 3, command = lambda: text_onButton(b13))
    b13.grid(row = 2, column = 2)
    b14 = Button(root, text = "", font = ("", 15), width = 8, height = 3, command = lambda: text_onButton(b14))
    b14.grid(row = 2, column = 3)
    b15 = Button(root, text = "", font = ("", 15), width = 8, height = 3, command = lambda: text_onButton(b15))
    b15.grid(row = 2, column = 4)

    b16 = Button(root, text = "", font = ("", 15), width = 8, height = 3, command = lambda: text_onButton(b16))
    b16.grid(row = 3, column = 0)
    b17 = Button(root, text = "", font = ("", 15), width = 8, height = 3, command = lambda: text_onButton(b17))
    b17.grid(row = 3, column = 1)
    b18 = Button(root, text = "", font = ("", 15), width = 8, height = 3, command = lambda: text_onButton(b18))
    b18.grid(row = 3, column = 2)
    b19 = Button(root, text = "", font = ("", 15), width = 8, height = 3, command = lambda: text_onButton(b19))
    b19.grid(row = 3, column = 3)
    b20 = Button(root, text = "", font = ("", 15), width = 8, height = 3, command = lambda: text_onButton(b20))
    b20.grid(row = 3, column = 4)

    b21 = Button(root, text = "", font = ("", 15), width = 8, height = 3, command = lambda: text_onButton(b21))
    b21.grid(row = 4, column = 0)
    b22 = Button(root, text = "", font = ("", 15), width = 8, height = 3, command = lambda: text_onButton(b22))
    b22.grid(row = 4, column = 1)
    b23 = Button(root, text = "", font = ("", 15), width = 8, height = 3, command = lambda: text_onButton(b23))
    b23.grid(row = 4, column = 2)
    b24 = Button(root, text = "", font = ("", 15), width = 8, height = 3, command = lambda: text_onButton(b24))
    b24.grid(row = 4, column = 3)
    b25 = Button(root, text = "", font = ("", 15), width = 8, height = 3, command = lambda: text_onButton(b25))
    b25.grid(row = 4, column = 4)

main()    
root.mainloop()