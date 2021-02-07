from tkinter import *
import requests
import json

root = Tk()
root.geometry("500x350")
s = StringVar()
root.config(bg = "lightgreen")
def show():
    url = "http://api.openweathermap.org/data/2.5/weather?q="+s.get()+"&appid=e55a2836a3153b9c51fccb6e97425256"
    api_request = requests.get(url)
    api_data = api_request.json()
    city = api_data["name"]
    wh = api_data["weather"][0]["main"]
    speed = api_data["wind"]["speed"]

    l = Label(root, text = f"City : {city}, Weather : {wh}, Speed : {speed}", font = ("", 15), bg = "lightgreen")
    l.place(x = 50, y = 125)

l = Label(root, text = "Here", font = ("", 15),bg = "lightgreen")
l.place(x = 50, y = 125)

l1 = Label(root, text = "Enter City : ", font = ("", 15),bg = "lightgreen")
l1.place(x = 95, y = 215)
name_city = Entry(root,font = ("", 15), textvariable = s)
name_city.place(x =201, y = 215)

b = Button(root, text = "Proceed", font = ("", 15), command = show)
b.place(x = 190, y = 265)
  
root.mainloop()