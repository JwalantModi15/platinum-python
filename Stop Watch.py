from tkinter import *
from datetime import datetime

root = Tk()
root.title("Stop Watch")
root.geometry("315x215")

def stop():
    global s
    l1["text"] = s
    root.after_cancel(Stop)
    b1["state"] = "normal"

def start():
    global i,j,s,k,Stop

    if k == 1:
        l1["text"] = "00:00"
        root.after_cancel(Stop)
        b1["state"] = "normal"

    elif i<=9:
        # s = "0"+str(j)+":0"
        s = str(k)+str(j)+":0"
        s = s + str(i)
        l1["text"] = s
        i+=1

    elif i>=10 and i<=59:
        # s = "0"+str(j)+":"
        s = str(k)+str(j)+":"
        s = s + str(i)
        l1["text"] = s
        i+=1

    elif j==9 and i==60:
        k+=1
        s = str(k)+"0:00"
        l1["text"] = s
        j=0
        i=0

    elif i==60:
        j+=1
        # s = "0"
        s = str(k)
        s = s + str(j)+":00"
        l1["text"] = s
        i=0

    if k==1:
        b1["state"] = "normal"
        i = 0
        j = 0
        k = 0
        s = ""
    else:
        b1["state"] = "disable"
        Stop = root.after(1000, start)

s = ""
i = 0
j = 0
k = 0

l1 = Label(root, text = "00:00", font = ("Arial", 41))
l1.pack(pady = 23)

b1 = Button(root, text = "Start", font = ("Arial", 15), command = start)
b1.place(x = 59, y = 125)

b2 = Button(root, text = "Stop", font = ("Arial", 15), command = stop)
b2.place(x = 185, y = 125)

root.mainloop()