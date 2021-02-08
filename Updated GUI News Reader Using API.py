from tkinter import *
import requests

root = Tk()
root.title("New Reader")
root.geometry("1000x700")
root.config(bg = "white")

def main(s1):
    news_text.config(state = "normal")
    news_text.delete("1.0",END)
    if s1 == "top headlines":
        url = "" // Here, News Headline API
        res = requests.get(url)
        data  = res.json()["articles"]
        s = ""
        n = 1
        news_text.insert(END, "Top Headlines\n\n")
        for i in data:
            s = s + str(n) + ". " + i["title"] + "\n\n\n"
            n+=1
        news_text.insert(END, s)
        news_text.config(state = "disable")

    else:
        url = "" // News API   
        res = requests.get(url)
        data  = res.json()["articles"]
        s = ""
        n = 1
        news_text.insert(END, s1.capitalize()+" Headlines"+"\n\n")
        for i in data:
            s = s + str(n) + ". " + i["title"] + "\n\n\n"
            n+=1
        news_text.insert(END, s)
        news_text.config(state = "disable")

url = "" // Here, News Headline API

res = requests.get(url)

data  = res.json()["articles"]
s = ""

scroll_v = Scrollbar(root)
scroll_v.pack(side = RIGHT, fill = Y)

scroll_h = Scrollbar(root, orient = 'horizontal')
scroll_h.pack(side =BOTTOM, fill = X)

news_text = Text(root, font = ("", 15), wrap = NONE, highlightthickness = 0, bd = 0, yscrollcommand = scroll_v.set, xscrollcommand = scroll_h.set)
news_text.pack(pady = 10,padx = 10, expand = True, fill=BOTH)

scroll_v.config(command = news_text.yview)
scroll_h.config(command = news_text.xview)
news_text.insert(END, "Top Headlines\n\n")
n = 1
for i in data:
    s = s + str(n) + ". " + i["title"] + "\n\n\n"
    n+=1
news_text.insert(END, s)

news_text.config(state = "disable")

main_menu = Menu(root)
choose_menu = Menu(main_menu, tearoff=0)
choose_menu.add_cascade(label = "technology", command = lambda : main("technology"))
choose_menu.add_cascade(label = "sports", command = lambda : main("sports"))
choose_menu.add_cascade(label = "business", command = lambda : main("business"))
choose_menu.add_cascade(label = "health", command = lambda : main("health"))
choose_menu.add_cascade(label = "entertainment", command = lambda: main("entertainment"))
choose_menu.add_cascade(label = "science", command = lambda : main("science"))
choose_menu.add_cascade(label = "top headlines", command = lambda : main("top headlines"))
main_menu.add_cascade(label = "News Topics", menu = choose_menu)
root.config(menu = main_menu)

root.mainloop()
