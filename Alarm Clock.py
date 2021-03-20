from tkinter import *
import pygame
from datetime import datetime

root = Tk()
root.title("Alarm")
root.geometry("500x300")

def set_alarm():
    time = datetime.today()
    now = time.strftime("%H:%M")
    if s.get() == now:
        music()
    else:
        root.after(500, set_alarm)

def stop():
    s.set("")
    pygame.mixer.music.pause()

def music():
    pygame.mixer.init()
    pygame.mixer.music.load(r"1.mp3")
    pygame.mixer.music.play()

l1 = Label(root, text = "Alarm Clock", font = ("", 21))
l1.pack(pady = 15)

l2 = Label(root, text = "Enter Hour and Minutes: ", font = ("", 15))
l2.place(x = 25, y = 100)

s = StringVar()

e1 = Entry(root, font = ("", 15), textvariable = s)
e1.place(x = 250, y = 102)

b1 = Button(root, text = "Set Alarm", font = ("", 15), command = set_alarm)
b1.place(x = 120, y = 190)

b2 = Button(root, text = "Stop", font = ("", 15), command = stop)
b2.place(x = 290, y = 190)

root.mainloop()
