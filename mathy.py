responses=["Welcome to Smart Calculator ThunderBolt","My name is Thunder","Thanks","Sorry","Hi How are You?","I am Fine","Ok,Stay Healthy"]
def extract_numbers_from_text(text):
    l=[]
    for t in text.split(" "):
        try:
            l.append(float(t))
        except:
            pass
    return(l)
def lcm(l):
    a = l[0]
    b = l[1]
    L=a if a>b else b
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L
        L+=1
def hcf(l):
    a = l[0]
    b = l[1]
    H = a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            return H
        H-=1
def add(l):
    s=0
    for i in l:
        s=s+i
    return s
def sub(l):
    s = l[0]
    i=1
    while i<len(l):
        s = s-l[i]
        i+=1
    return s
def multiply(l):
    m=1
    for i in l:
        m=m*i
    return m
def division(l):
    d = l[0]
    i=1
    while i<len(l):
        d = d/l[i]
        i+=1
    return d
def end():
    print(responses[2])
    exit()
def myname():
    print(responses[1])
def hi():
    print(responses[4])
def how():
    print(responses[5])
def fine():
    print(responses[6])
def sorry():
    print(responses[3])

operations = {"PLUS":add,"ADD":add,"ADDITION":add,"SUM":add,"+":add,"-":sub,"MINUS":sub,"SUBSTRACTION":sub,"SUBSTRACT":sub,"PRODUCT":multiply,"MULTIPLICATION":multiply,
              "MULTIPLY":multiply,"MULTIPLE":multiply,"*":multiply,"DIVIDE":division,"DIVISION":division,"/":division,"HCF":hcf,"LCM":lcm}

commands = {"NAME":myname,"END":end,"EXIT":end,"CLOSE":end,"EXIT":end,"HI":hi,"HOW":how,"FINE":fine,"GOOD":fine}
    
              


