from tkinter import *
from itertools import cycle
from random import randrange,choice
from tkinter import messagebox

canvas_width = 800
canvas_height = 450

root = Tk()
root.title("EggCatchersGame")
c = Canvas(root, width = canvas_width, height = canvas_height, bg = "deepskyblue")
c.create_rectangle(-5, canvas_height - 100, canvas_width+5, canvas_height+5, fill = "seagreen", width =0)
c.create_oval(-80,-80, 120, 120, fill = "orange", width=0)
c.pack()

egg_width = 45
egg_height = 55
egg_score = 10
egg_speed = 450
egg_interval = 5000
difficulty_factor = 0.9
catcher_color = "blue"
catcher_width = 100
catcher_height = 100
catcher_start_x = canvas_width/2-catcher_width/2
catcher_start_y = canvas_height-catcher_height-25 
catcher_start_x2 = catcher_start_x+catcher_width
catcher_start_y2 = catcher_start_y+catcher_height

catcher = c.create_arc(catcher_start_x, catcher_start_y, catcher_start_x2, catcher_start_y2, start = 200, extent = 140,style = "arc", outline = catcher_color,width = 2.3)


score = 0
score_text = c.create_text(10,10, anchor = 'nw', font = ("", 18), fill = "darkblue", text = "Your Score : "+str(score))

lives_remaining = 3
lives_text = c.create_text(canvas_width-10,10, anchor = 'ne', font = ("", 18), fill = "darkblue", text = "Lives : "+str(lives_remaining))

eggs=[]

colors = cycle(["skyblue", "gold", "lightgreen", "lightpink", "white"])
  
def create_eggs():
    x = randrange(10, 740)
    y = 0
    new_egg = c.create_oval(x,y,x+egg_width, y+egg_height, fill = next(colors), width=0)
    eggs.append(new_egg)
    root.after(egg_interval, create_eggs)
    
def move_eggs():    
    for egg in eggs:
        (egg_x,egg_y,egg_x2,egg_y2) = c.coords(egg)
        c.move(egg,0,15)
        if egg_y2>canvas_height:
            egg_dropped(egg)
    root.after(egg_speed, move_eggs)        

def egg_dropped(egg):
    global egg_speed, egg_interval, score, lives_remaining,ch
    eggs.remove(egg)
    c.delete(egg)
    lose_a_life()
    if lives_remaining==0:
        messagebox.showinfo("Game Over", "Final Score : "+str(score))
        messagebox.showinfo("One More Time", "Press Ok to Play Again!")
        egg_speed = 650
        egg_interval = 7000
        score = 0
        lives_remaining = 3 
        for egg in eggs:
            c.delete(egg)
        eggs.clear()
        c.itemconfigure(score_text, text = "Your Score : "+str(score))
        c.itemconfigure(lives_text, text = "Lives : "+str(lives_remaining))
        create_eggs()

def lose_a_life():
    global lives_remaining
    lives_remaining-=1
    c.itemconfigure(lives_text, text = "Lives : "+str(lives_remaining))        

def catch():
    global egg_score,ch
    (catcher_x, catcher_y, catcher_x2, catcher_y2) = c.coords(catcher)
    for egg in eggs:
        (egg_x, egg_y, egg_x2, egg_y2) = c.coords(egg)
        if egg_x>catcher_x and egg_x2 < catcher_x2 and catcher_y2 - egg_y2 < 45:
                eggs.remove(egg)
                c.delete(egg)   
                increase_score(egg_score)
    root.after(100, catch)

def increase_score(points):
    global score, egg_speed, egg_interval
    score+=points
    egg_speed = int(egg_speed*difficulty_factor)
    egg_interval = int(egg_interval*difficulty_factor)
    c.itemconfigure(score_text, text = "Your Score : "+str(score))

def move_left(e):
    (x1,y1,x2,y2) = c.coords(catcher)
    if x1>8:
        c.move(catcher, -21,0)
        
def move_right(e):
    (x1,y1,x2,y2) = c.coords(catcher)
    if x2<canvas_width-8:
        c.move(catcher, 21,0)

c.bind("<Left>", move_left)
c.bind("<Right>", move_right)
c.focus_set()        

root.after(5000, create_eggs)
root.after(5000, move_eggs)
root.after(5000, catch)
   
root.mainloop()