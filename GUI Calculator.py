from tkinter import *
from math import*
root = Tk()
root.geometry("447x330")
root.resizable(0,0)
root.title("GUI Calculator")
a = StringVar()
def show(c):
    if not len(a.get()+c)>18:
        a.set(a.get()+c)
    else:
        a.set("Error")      
def equal():
    expression = a.get()
    a.set(eval(expression))
def squareRoot():
    n=float(a.get())
    a.set(sqrt(n))
def square():
    n=a.get()
    a.set(float(n)**2)       
def cancel():
    a.set("")
def clear():
    e = a.get()
    a.set(e[:-1])    
e1 = Entry(font = ("", 30), justify = "right", textvariable = a, bg = "light gray", relief = "solid", bd = 3)
e1.place(x=0,y=0,width = 447, height = 50)

b1 = Button(text = "7", font = ("", 25), bg = "gray", fg = "white", activeforeground = "red")
b1.place(x=5, y = 55, width = 105, height = 50)
b1.configure(command = lambda: show("7"))
root.bind("<Key-7>", lambda e: show("7"))

b2 = Button(text = "8", font = ("", 25), bg = "gray", fg = "white", activeforeground = "red")
b2.place(x=115, y = 55, width = 105, height = 50)
b2.configure(command = lambda: show("8"))
root.bind("<Key-8>", lambda e: show("8"))

b3 = Button(text = "9", font = ("", 25), bg = "gray", fg = "white", activeforeground = "red")
b3.place(x=225, y = 55, width = 105, height = 50)
b3.configure(command = lambda: show("9"))
root.bind("<Key-9>", lambda e: show("9"))

b4 = Button(text = "C", font = ("", 25), bg = "gray", fg = "white", activeforeground = "red")
b4.place(x=335, y = 55, width = 105, height = 50)
b4.configure(command = cancel)
root.bind("<BackSpace>", lambda e: clear())

b5 = Button(text = "4", font = ("", 25), bg = "gray", fg = "white", activeforeground = "red")
b5.place(x=5, y = 110, width = 105, height = 50)
b5.configure(command = lambda: show("4"))
root.bind("<Key-4>", lambda e: show("4"))

b6 = Button(text = "5", font = ("", 25), bg = "gray", fg = "white", activeforeground = "red")
b6.place(x=115, y = 110, width = 105, height = 50)
b6.configure(command = lambda: show("5"))
root.bind("<Key-5>", lambda e: show("5"))

b7 = Button(text = "6", font = ("", 25), bg = "gray", fg = "white", activeforeground = "red")
b7.place(x=225, y = 110, width = 105, height = 50)
b7.configure(command = lambda: show("6"))
root.bind("<Key-6>", lambda e: show("6"))

b8 = Button(text = "x", font = ("", 25), bg = "gray", fg = "white", activeforeground = "red")
b8.place(x=335, y = 110, width = 105, height = 50)
b8.configure(command = clear)
root.bind("<BackSpace>", lambda e: clear())

b9 = Button(text = "1", font = ("", 25), bg = "gray", fg = "white", activeforeground = "red")
b9.place(x=5, y = 165, width = 105, height = 50)
b9.configure(command = lambda: show("1"))
root.bind("<Key-1>", lambda e: show("1"))

b10 = Button(text = "2", font = ("", 25), bg = "gray", fg = "white", activeforeground = "red")
b10.place(x=115, y = 165, width = 105, height = 50)
b10.configure(command = lambda: show("2"))
root.bind("<Key-2>", lambda e: show("2"))

b11 = Button(text = "3", font = ("", 25), bg = "gray", fg = "white", activeforeground = "red")
b11.place(x=225, y = 165, width = 105, height = 50)
b11.configure(command = lambda: show("3"))
root.bind("<Key-3>", lambda e: show("3"))

b12 = Button(text = "+", font = ("", 25), bg = "gray", fg = "white", activeforeground = "red")
b12.place(x=335, y = 165, width = 105, height = 50)
b12.configure(command = lambda: show("+"))
root.bind("<Key-+>", lambda e: show("+"))

b13 = Button(text = "0", font = ("", 25), bg = "gray", fg = "white", activeforeground = "red")
b13.place(x=5, y = 220, width = 105, height = 50)
b13.configure(command = lambda: show("0"))
root.bind("<Key-0>", lambda e: show("0"))

b14 = Button(text = ".", font = ("", 25), bg = "gray", fg = "white", activeforeground = "red")
b14.place(x=115, y = 220, width = 105, height = 50)
b14.configure(command =lambda: show("."))
root.bind("<Key-.>", lambda e: show("."))

b15 = Button(text = "=", font = ("", 25), bg = "gray", fg = "white", activeforeground = "red")
b15.place(x=225, y = 220, width = 105, height = 50)
b15.configure(command = equal)
root.bind("<Key-=>", lambda e: equal())

b16 = Button(text = "-", font = ("", 25), bg = "gray", fg = "white", activeforeground = "red")
b16.place(x=335, y = 220, width = 105, height = 50)
b16.configure(command = lambda: show("-"))
root.bind("<minus>", lambda e: show("-"))

b17 = Button(text = "x^2", font = ("", 25), bg = "gray", fg = "white", activeforeground = "red")
b17.place(x=5, y = 275, width = 105, height = 50)
b17.configure(command = square)

b18 = Button(text = "sqrt(x)", font = ("", 25), bg = "gray", fg = "white", activeforeground = "red")
b18.place(x=115, y = 275, width = 105, height = 50)
b18.configure(command = squareRoot)

b19 = Button(text = "/", font = ("", 25), bg = "gray", fg = "white", activeforeground = "red")
b19.place(x=225, y = 275, width = 105, height = 50)
b19.configure(command = lambda: show("/"))
root.bind("<Key-/>", lambda e: show("/"))

b20 = Button(text = "*", font = ("", 25), bg = "gray", fg = "white", activeforeground = "red")
b20.place(x=335, y = 275, width = 105, height = 50)
b20.configure(command = lambda: show("*"))
root.bind("<Key-*>", lambda e: show("*"))

root.mainloop()