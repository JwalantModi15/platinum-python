from tkinter import *
def clear():
    textin.set("")

def extract_num():
    l = []
    text = textin.get()
    for t in text.split(" "):
        try:
            l.append(float(t))
        except:
            pass
    return l        

def extract_ope():
    text = textin.get()
    list_oper = []
    for t in text.split(" "):
        try:
            list_oper.append(operations[t.upper()])
        except:
            pass
    return list_oper 
def cal(num, ope):
    c,j=0,0
    length = len(num)
    exp=""
    for i in num:
        exp = exp+str(i)
        c+=1
        if c==length:
            break
        while j<c:
            exp = exp+ope[j]
            j+=1        
    ans = eval(exp)       
    return ans                              
def hcf(a,b):
    h = a if a<b else b
    while h>=1:
        if a%h==0 and b%h==0:
            return h
        h-=1     
def lcm(a,b):
    l = a if a>b else b
    while l<=a*b:
        if l%a==0 and l%b==0:
            return l
        l+=1    

def show():
    t = textin.get()
    for word in t.split(" "):
        if word.upper()=="HCF" or word.upper()=="LCM":
            try:
                n = extract_num()
                r = operations[word.upper()](n[0], n[1])
                libox.delete(0,END)
                libox.insert(END, r)
                libox.after(1500, clear)
            except:
                libox.delete(0,END)
                libox.insert(END, "Something went wrong Please Enter Valid Input")    
            finally:
                return

        elif word.upper() in operations.keys():
            try:
                n = extract_num()
                o = extract_ope()
                calculate = cal(n,o)
                libox.delete(0,END)
                libox.insert(END, calculate)
                libox.after(1500, clear)
            except:
                libox.delete(0,END)
                libox.insert(END, "Something went wrong Please Enter Valid Input")    
            finally:
                return    
        else:
            libox.delete(0,END)
            libox.insert(END, "Something went wrong Please Enter Valid Input")         


operations = {"PLUS":'+',"ADD":"+","ADDITION":"+","SUM":"+","+":"+",
              "-":"-","MINUS":"-","SUBSTRACTION":"-","SUBSTRACT":"-","SUB":'-',
              "PRODUCT":"*","MULTIPLICATION":"*",
              "MULTIPLY":"*","MULTIPLE":"*","*":"*",
              "DIVIDE":"/","DIVISION":"/","/":"/",
              "HCF":hcf,"LCM":lcm}
             

root = Tk()
root.title("Smart Calculator")
root.geometry("500x400")
root.configure(bg = "lightblue")

l1 = Label(root, text = "I am Smart Calculator", width = 23, font = ("", 12))
l1.place(x=135, y=10)

l2 = Label(root, text = "My name is Thunder!", font = ("", 12), padx = 10)
l2.place(x=163, y=50)

l3 = Label(root, text = "What can I help you?", font = ("", 12))
l3.place(x=173, y=100)

l4 = Label(root, text = "Please Write Queries below seperated by space!", font = ("", 12))
l4.place(x=85, y=135)

textin = StringVar()
e1 = Entry(root, width = 41,textvariable = textin, font = ("", 12))
e1.place(x=72, y = 180,  height = 32)

b1 = Button(root, text = "Answer", font = ("", 12), command = show)
b1.place(x=208, y = 235)

libox = Listbox(root, width = 41, height = 5, font = ("", 12))
libox.place(x = 70, y = 280)
root.mainloop()