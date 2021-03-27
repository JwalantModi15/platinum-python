from tkinter import *
from tkinter import messagebox
import random
import pygame
root = Tk()
root.title("Tic Tac Toe")
root.geometry("366x360")

def main(button, i):
    if(button["text"] == ""):
        button["text"] = "O"
        index_list.remove(i)
        if winner("O"):
            messagebox.showinfo("Congratulations!","Player 'O' Wins!")
            reset()
            
        if Tie():
            messagebox.showinfo("Tie!","Match Ties!")
            reset()

        n1 = AI()
        index_list.remove(n1)
        b[n1]["text"] = "X"
        if winner("X"):
            messagebox.showinfo("Congratulations!","Player 'X' Wins!")
            reset()

        if Tie():
            messagebox.showinfo("Tie!","Match Ties!")
            reset() 

def Tie():
    for i in range(9):
        if b[i]["text"] == "":
            return False
    else:
        return True

def AI():
    count=0
    # n = random.randint(0,8)
    # while n in index_list:
    #     n = random.randint(0,8)
    for i in ["O","X"]:
        for j in index_list:
            b[j]["text"] = i
            if winner(i):
                b[j]["text"] = ""
                count=1
                print("AI",j)
                return j
            b[j]["text"] = ""

    if(count==0):
        # n = random.randint(0,8)
        # while n in index_list:
        #     n = random.randint(0,8)
        n = random.choice(index_list)
        print("Random",n)
        return n          

def winner(s):
    return ((b[0]["text"]==s and b[1]["text"]==s and b[2]["text"]==s) or 
            (b[3]["text"]==s and b[4]["text"]==s and b[5]["text"]==s) or
            (b[6]["text"]==s and b[7]["text"]==s and b[8]["text"]==s) or 
            (b[0]["text"]==s and b[3]["text"]==s and b[6]["text"]==s) or
            (b[1]["text"]==s and b[4]["text"]==s and b[7]["text"]==s) or
            (b[2]["text"]==s and b[5]["text"]==s and b[8]["text"]==s) or 
            (b[0]["text"]==s and b[4]["text"]==s and b[8]["text"]==s) or
            (b[2]["text"]==s and b[4]["text"]==s and b[6]["text"]==s))

def reset():
    global index_list
    for i in range(9):
        b[i]["text"] = ""

    index_list = [0,1,2,3,4,5,6,7,8]    
    pygame.mixer.music.play()

b = []
c=1
index_list = [0,1,2,3,4,5,6,7,8]
pygame.mixer.init()
pygame.mixer.music.load(r"C:\Users\Jwalant Modi\Music\1.mp3")
pygame.mixer.music.play()
for i in range(3):
    for j in range(3):
        b1 = Button(root, text = "", font = ("Arial", 21), width = 7, height = 3)
        b1.grid(row = i, column = j)
        b.append(b1)

b[0].configure(command = lambda: main(b[0],0))
b[1].configure(command = lambda: main(b[1],1))
b[2].configure(command = lambda: main(b[2],2))

b[3].configure(command = lambda: main(b[3],3))
b[4].configure(command = lambda: main(b[4],4))
b[5].configure(command = lambda: main(b[5],5))

b[6].configure(command = lambda: main(b[6],6))
b[7].configure(command = lambda: main(b[7],7))
b[8].configure(command = lambda: main(b[8],8))

root.mainloop()