from tkinter import *
from tkinter import colorchooser
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk,ImageGrab
from tkinter import ttk
def save():
    global c
    file_name = asksaveasfilename(defaultextension = ".jpg", filetypes = [("Images in jpg","*.jpg"),("Images in png", "*.png")] )  
    x = root.winfo_rootx()+90+c.winfo_x()
    y = root.winfo_rooty()+95+c.winfo_y()
    x1 = x+c.winfo_width()+70
    y1 = y+c.winfo_height()+30
    ImageGrab.grab().crop((x,y,x1,y1)).save(file_name)

def open_file():
    file_name = askopenfilename(defaultextension = ".jpg", filetypes = [("Images","*.jpg"),("All Images", "*.*")])
    image = Image.open(file_name)
    image.show()
    

def choose_color():
    color = colorchooser.askcolor(title = "Choose Color")
    c["bg"] = color[1]

def clear():
    c.delete("all")

def brush_color():
    global pen_color
    color = colorchooser.askcolor(title = "Choose Color")
    pen_color = color[1]

def start(event):
    global last_x, last_y
    last_x = event.x
    last_y = event.y

def draw(event):
    global pen_color, brush_size, last_x, last_y
    brush_size = size.get()
    x2 = event.x
    y2 = event.y
    line = c.create_line(last_x,last_y,x2,y2, fill =pen_color, width = brush_size)
    last_x,last_y = x2,y2

def eraser():
    global pen_color,brush_size
    pen_color = c["bg"] 


root = Tk()
root.title("My Paint App")
root.geometry("800x580")

last_x,last_y = 0,0
pen_color = "red"
brush_size = 3
file_name = None
size = IntVar()

Menubar = Menu(root)
fileMenu = Menubutton(Menubar)
Menubar.add_cascade(label = "Save", menu = fileMenu, command = save)

open_Menu = Menubutton(Menubar)
Menubar.add_cascade(label = "Open", menu = open_Menu, command = open_file)

color_menu = Menubutton(Menubar)
# color_menu.add_command(label = "Choose Color", command = choose_color)
Menubar.add_cascade(label= "Background Color", menu = color_menu, command = choose_color)

brush_menu = Menubutton(Menubar)
# brush_menu.add_command(label = "Choose Color", command = brush_color)
Menubar.add_cascade(label= "Brush Color", menu = brush_menu, command = brush_color)


Size = [1,2,3,4,5,6,7,8,9,10,12]

size_menu = Menu(Menubar, tearoff=0)
c=0
for j in Size:
    size_menu.add_radiobutton(label = j, variable = size)
    c+=1
Menubar.add_cascade(label = "Brush Size", menu = size_menu)

eraser_Menu = Menubutton(Menubar)
Menubar.add_cascade(label = "Eraser", menu = eraser_Menu, command = eraser)

clear_menu = Menubutton(Menubar)
# clear_menu.add_command(label = "Clear All", command = clear)
Menubar.add_cascade(label= "Clear", menu = clear_menu, command = clear)

root.config(menu = Menubar)

c = Canvas(root, width = 800, height = 580)
c.pack()
c.bind("<B1-Motion>", draw)
c.bind("<Button-1>", start)



root.mainloop()
