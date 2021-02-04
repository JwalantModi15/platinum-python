from tkinter import *
import random
import time
c=0
def show_symbols(x,y):
    global pre_x, pre_y, first, buttons, button_symbols, symbols, root, c
    buttons[x,y]["text"] = button_symbols[x,y]
    buttons[x,y].update_idletasks()

    if first:
        pre_x = x
        pre_y = y
        first = False

    elif pre_x!=x or pre_y!=y:
        if buttons[pre_x, pre_y]["text"] != buttons[x,y]["text"]:
            time.sleep(0.5)
            buttons[pre_x, pre_y]["text"] = ""
            buttons[x,y]["text"] = ""
        else:
            c+=1 
            buttons[pre_x, pre_y]["command"] = DISABLED   
            buttons[x, y]["command"] = DISABLED
            if c==12:
                time.sleep(1.5)
                for x in range(4):
                    for y in range(6):
                        buttons[x,y]["text"] = ""
                        main()
        first = True    


first = True
pre_x = 0
pre_y = 0
buttons = {}
button_symbols = {}
symbols = ["A", "B", "C", "D", "E","1", "@", "3", "4","5", "$",
            "#","A", "B", "C", "D", "E","1", "@", "3", "4","5", "$",
            "#"]

root = Tk()
root.resizable(0,0)
root.title("The MatchMaker")
def main():
    global button_symbols, buttons, symbols
    i=0
    random.shuffle(symbols)
    for x in range(4):
        for y in range(6):
            b = Button(command = lambda x=x,y=y: show_symbols(x,y), width = 8, height = 5, font=("",15))
            b.grid(row = x, column = y)
            buttons[x,y] = b
            button_symbols[x,y] = symbols[i]
            i+=1
main()                        
root.mainloop()         
        
