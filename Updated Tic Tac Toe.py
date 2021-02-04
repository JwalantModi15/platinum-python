from tkinter import *
from tkinter import messagebox
c=1
co=1
def show(b):
    global c
    c = c+1
    if(b["text"]==""):
        if (c%2==0):
            b["text"] = "O"
        else:
            b["text"] = "X"   

    # for "O" Player        
    if b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O" or b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O" or b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O":
        if b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O":
            b1["bg"] = "red"
            b2["bg"] = "red"
            b3["bg"] = "red"

        elif b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O":
            b4["bg"] = "red"
            b5["bg"] = "red"
            b6["bg"] = "red"
        elif b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O":
            b7["bg"] = "red"
            b8["bg"] = "red"
            b9["bg"] = "red"
        messagebox.showinfo("Congratulation", "Player 'O' Wins")    


        
    elif b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O" or b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O" or b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O":    
       
        if b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O":
            b1["bg"] = "red"
            b4["bg"] = "red"
            b7["bg"] = "red"

        elif b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O":
            b2["bg"] = "red"
            b5["bg"] = "red"
            b8["bg"] = "red"
        elif b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O":
            b3["bg"] = "red"
            b6["bg"] = "red"
            b9["bg"] = "red"

        messagebox.showinfo("Congratulation", "Player 'O' Wins")     
       
    elif b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O" or b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O":    
      
        if b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O":
            b1["bg"] = "red"
            b5["bg"] = "red"
            b9["bg"] = "red"

        elif b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O":
            b3["bg"] = "red"
            b5["bg"] = "red"
            b7["bg"] = "red"

        messagebox.showinfo("Congratulation", "Player 'O' Wins") 

    # Player 'X'    
    elif b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X" or b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X" or b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X":
     
        if b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X":
            b1["bg"] = "red"
            b2["bg"] = "red"
            b3["bg"] = "red"

        elif b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X":
            b4["bg"] = "red"
            b5["bg"] = "red"
            b6["bg"] = "red"
        elif b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X":
            b7["bg"] = "red"
            b8["bg"] = "red"
            b9["bg"] = "red"

        messagebox.showinfo("Congratulation", "Player 'X' Wins")     
       
    elif b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X" or b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X" or b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X":    
        
        if b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X":
            b1["bg"] = "red"
            b4["bg"] = "red"
            b7["bg"] = "red"

        elif b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X":
            b2["bg"] = "red"
            b5["bg"] = "red"
            b8["bg"] = "red"
        elif b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X":
            b3["bg"] = "red"
            b6["bg"] = "red"
            b9["bg"] = "red"

        messagebox.showinfo("Congratulation", "Player 'X' Wins")    
       
    elif b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X" or b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X":

        if b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X":
            b1["bg"] = "red"
            b5["bg"] = "red"
            b9["bg"] = "red"

        elif b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X":
            b3["bg"] = "red"
            b5["bg"] = "red"
            b7["bg"] = "red"

        messagebox.showinfo("Congratulation", "Player 'X' Wins")    

    elif b1["text"]!="" and b2["text"]!="" and b3["text"]!="" and b4["text"]!="" and b5["text"]!="" and b6["text"]!="" and b7["text"]!="" and b8["text"]!="" and b9["text"]!="":
        messagebox.showinfo("Better Luck Next Time", "Tie")
                 
def again ():
    b1["text"]=""
    b2["text"]=""
    b3["text"]="" 
    b4["text"]="" 
    b5["text"]="" 
    b6["text"]="" 
    b7["text"]=""
    b8["text"]="" 
    b9["text"]=""
    b1["bg"]="white"
    b2["bg"]="white"
    b3["bg"]="white" 
    b4["bg"]="white" 
    b5["bg"]="white" 
    b6["bg"]="white" 
    b7["bg"]="white"
    b8["bg"]="white" 
    b9["bg"]="white"                              
def main():
    global root
    root = Tk()
    root.geometry("358x395")
    root.resizable(0,0)
    root.title("TIC TAC TOE")
    global b1,b2,b3,b4,b5,b6,b7,b8,b9,l
    Menubar = Menu(root)
    menu_option = Menubutton(Menubar)
    Menubar.add_cascade(label = "Reset the Game", menu = menu_option, command = again)
    root.config(menu = Menubar)


    b1 = Button(root,width = 10, height = 5, font = ("Arial", 15), text = "", command = lambda: show(b1))
    b1.grid(row = 0, column = 0)
    b2 = Button(root,width = 10, height = 5, font = ("Arial", 15), text = "", command = lambda: show(b2))
    b2.grid(row = 0, column = 1)
    b3 = Button(root,width = 10, height = 5, font = ("Arial", 15), text = "", command = lambda: show(b3))
    b3.grid(row = 0, column = 2)
    b4 = Button(root,width = 10, height = 5, font = ("Arial", 15), text = "", command = lambda: show(b4))
    b4.grid(row = 1, column = 0)
    b5 = Button(root,width = 10, height = 5, font = ("Arial", 15), text = "", command = lambda: show(b5))
    b5.grid(row = 1, column = 1)
    b6 = Button(root,width = 10, height = 5, font = ("Arial", 15), text = "", command = lambda: show(b6))
    b6.grid(row = 1, column = 2)
    b7 = Button(root,width = 10, height = 5, font = ("Arial", 15), text = "", command = lambda: show(b7))
    b7.grid(row = 2, column = 0)
    b8 = Button(root,width = 10, height = 5, font = ("Arial", 15), text = "", command = lambda: show(b8))
    b8.grid(row = 2, column = 1)
    b9 = Button(root,width = 10, height = 5, font = ("Arial", 15), text = "", command = lambda: show(b9))
    b9.grid(row = 2, column = 2)
    
    root.mainloop()
main()
