from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
from tkinter import ttk
def newFile(e):
    global file
    root.title("Untitled-Notepad")
    file = None
    TextArea.delete(1.0, END)


def openFile(e):
    global file
    file = askopenfilename(defaultextension = ".txt", filetypes = [("All Files", "*.*"),("Text Documents", "*.txt")])
    if file!="":
        root.title(os.path.basename(file)+"-Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()
    else:
        file = None    


def saveFile(e):
    global file
    if file==None:
        file = asksaveasfilename(initialfile = "Untitled.txt", defaultextension = ".txt", filetypes = [("All Files", "*.*"),("Text Documents", "*.txt")])

        if file!="":
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file)+"-Notepad")
        else:
            file = None     

    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()

def cut():
    TextArea.event_generate(("<<Cut>>"))

def copy():
    TextArea.event_generate(("<<Copy>>"))

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    messagebox.showinfo("About", "NotePad is Created by Jwalant")
def exit_notepad():
    root.destroy()
    
def chooseSize():
    TextArea["font"] = ("",size.get())

def chooseColor():
    if color.get()=="black":
        TextArea["bg"] = "black"
        TextArea["fg"] = "white"
        TextArea["insertbackground"] = "white"
    
    else:
        TextArea["bg"] = color.get()
        TextArea["fg"] = "black"
        TextArea["insertbackground"] = "black"

def contact():
    messagebox.showinfo("Contact", "My Email: jwalantmodi05@gmail.com")
root = Tk()
root.title("Untitled-Notepad")
root.geometry("700x500")
# root.wm_iconbitmap("notepad.ico")
TextArea = Text(root, font = ("Arial", 12))
TextArea.focus_set()
TextArea.pack(expand = True,fill=BOTH)

file = None

Menubar = Menu(root)
Filemenu = Menu(Menubar, tearoff=0)
Filemenu.add_command(label = "New", command = lambda : newFile(1))
Filemenu.add_command(label = "Open", command = lambda: openFile(1))
Filemenu.add_command(label = "Save", command = lambda: saveFile(1))
Filemenu.add_separator()
Filemenu.add_command(label = "Exit", command = exit_notepad)
Menubar.add_cascade(label = "File", menu = Filemenu)

Editmenu = Menu(Menubar, tearoff=0)
Editmenu.add_command(label = "Cut", command = cut)
Editmenu.add_command(label = "Copy", command = copy)
Editmenu.add_command(label = "Paste", command = paste)
Menubar.add_cascade(label = "Edit", menu = Editmenu)

color = StringVar()
dict_color = {1:"white", 2:"lightblue", 3:"lightgreen", 4:"lightgray", 5:"black"}
colorMenu = Menu(Menubar, tearoff=0)

for i in dict_color:
    colorMenu.add_radiobutton(label = dict_color[i], command = chooseColor, variable = color)
Menubar.add_cascade(label = "Color", menu = colorMenu)

Size = [10,12,14,16,18,20,22,24,26,28,30]
size = IntVar()
sizeMenu = Menu(Menubar, tearoff=0)
c=0
for j in Size:
    sizeMenu.add_radiobutton(label = j, command = chooseSize, variable = size)
    c+=1
Menubar.add_cascade(label = "Font Size", menu = sizeMenu)

Helpmenu = Menu(Menubar, tearoff = 0)
Helpmenu.add_command(label="About Notes", command = about)
Helpmenu.add_command(label="Contact", command = contact)
Menubar.add_cascade(label = "Help", menu = Helpmenu)

root.config(menu = Menubar)
TextArea.bind("<Control-n>", newFile)
TextArea.bind("<Control-o>", openFile)
TextArea.bind("<Control-s>", saveFile)

scroll = Scrollbar(TextArea)
scroll.pack(side = RIGHT, fill = Y)
scroll.config(command = TextArea.yview)
TextArea.config(yscrollcommand = scroll.set)

status_bar = ttk.Label(root, text = "Status Bar")
status_bar.pack(side = BOTTOM)

def status(e):
    if TextArea.edit_modified():
        words = len(TextArea.get(1.0, END).split(" "))
        letters = len(TextArea.get(1.0, END))
        status_bar.config(text = f"Words: {words} and Letters: {letters}")
    TextArea.edit_modified(False)    

TextArea.bind("<<Modified>>", status)
root.mainloop()
