from tkinter import *
import os
import pygame
pygame.mixer.init()
n=0
def music_():
    global old_song

    if s.get()!=old_song:
        old_song = s.get()
        song = s.get()
        pygame.mixer.music.load("Music/"+song)
        pygame.mixer.music.play()
        b1.config(text = "Pause") 

def music_pause():
    global n
    n=n+1 

    if n%2==0:
        pygame.mixer.music.pause()
        b1.config(text = "UnPause")
    else:
        pygame.mixer.music.unpause()
        b1.config(text = "Pause") 
       



root = Tk()
root.geometry("405x210")

l = Label(root, text = "Music Player", font = ("Arial", 30, "bold"))
l.place(x=73, y = 25)

s = StringVar()
s.set("Select Music")
old_song = s.get()

choices = os.listdir("C:Music")
choices = choices[:-1]

b = Button(root, text = "Play", width = 21, command = music_, font = ("",10))
b.place(x = 50, y = 105)

b1 = Button(root, text = "Pause", width = 21, command = music_pause, font = ("", 10))
b1.place(x = 100, y = 158)

menu = OptionMenu(root, s, *choices)
menu.place(x = 250, y = 105)


root.mainloop()
