from tkinter import *
import os
import requests

os.chdir(r"C:\Users\Jwalant Modi\1")
root = Tk()
root.title("BitCoin")
root.geometry("550x210")
root.config(bg = "black")

def update():
    global data
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    res = requests.get(url)
    data = res.json()
    # print(data)
    bit_label.config(text = data["bpi"]["USD"]["rate"])
    last_update()
    root.after(30000, update)

def last_update():
    global data
    a = data["time"]["updated"]
    time_label.config(text = "Updated at "+ a)
    root.after(30000, last_update)

f1 = Frame(root, bg = "black")
f1.pack(pady = 21)
global data
logo = PhotoImage(file = "bitcoin.png")
logo_label = Label(f1, image = logo, bd = 0)
logo_label.grid(row = 0, column = 0, rowspan = 2)

bit_label = Label(f1, text = "Test", font = ("Arial", 45), bg = "black", fg = "green", bd = 0)
bit_label.grid(row = 0, column = 1, padx = 21, sticky = "s")

time_label = Label(f1, text = "Price", font = ("Arial", 15), bg = "black", fg = "grey")
time_label.grid(row = 1, column = 1, sticky = "n")

update()
root.mainloop()
