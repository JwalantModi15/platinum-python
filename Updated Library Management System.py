class Library:
    def __init__(self,d,name):
        self.Dict_books = d
        self.lib_name = name
        self.init_lib = {}
    def display(self):
        print("Available Books are: ")
        print("----------------")
        print("Books")
        for i in self.Dict_books.items():
            print(i)
        print("----------------")    
    def issue(self,name,i,book,c=0):
        if self.Dict_books[book] == 0:
            print("No Book left")
            print("Please wait untill anyone return the book")
        elif book not in self.Dict_books.keys():
                print("Please Enter Right Detail of name and book")
        else:
            if len(self.init_lib)==0:
                self.init_lib.update({i:book})
                self.Dict_books[book] = self.Dict_books[book]-1
                if c==0:
                    print("Book is Issued Successfully!")
            elif i in self.init_lib.keys():
                self.init_lib[i] = self.init_lib[i]+","+book
                self.Dict_books[book] = self.Dict_books[book]-1
                if c==0:
                    print("Book is Issued Successfully!")
            elif i not in self.init_lib.keys():
                self.init_lib.update({i:book})
                self.Dict_books[book] = self.Dict_books[book]-1
                if c==0:
                    print("Book is Issued Successfully!")
            else:    
                print("Book is already issued to you")

    def return_book(self,name,i,book):
        if i in self.init_lib.keys():
            d = self.init_lib[i]
            l1 = d.split(",")
            if len(l1)==1  and book in self.init_lib.values():
                b = self.init_lib.pop(i)
                self.Dict_books[b] = self.Dict_books[b]+1
                print("Book Returns Successfully!")
            elif len(l1)>1:
                if book not in l1:
                    print("There is no such book related with your name")
                else:
                    l=[]
                    b = self.init_lib.pop(i)
                    l = b.split(",")
                    for j in l:
                        if j==book:
                            self.Dict_books[j] = self.Dict_books[j]+1
                        else:
                            self.Dict_books[j] = self.Dict_books[j]+1
                            self.issue(name,i,j,1)
            else:
                print("There is no such book related with your name")
        else:
            print("There is No book related with your name.")
    def book_hol(self):
        print("ID of Person | Name of Book")
        for i in self.init_lib:
            print("    ", i,"           ",self.init_lib[i])  
              
    def add_book(self,book):
        self.list_books.append(book)


d = {"python":3,"c language":2,"c++ language":3,"ancyclopedia":1,"india":5,"dbms":3,"the alchemist":1,"sql":5}
l = Library(d,"Thunder")
print(f"Welcomes to '{l.lib_name}' Library")
while True:
    print("\n1.Display the availabe books: ")
    print("\n2.Issue any Book: ")
    print("\n3.Return any Book: ")
    print("\n4.Current Books holding status: ")
    print("\n5.Quit")
    print("\nEnter Your Choice (1,2,3,4)")
    n = int(input("\nEnter: "))

    if n==1:
        l.display()
    if n==2:
        x = input("Enter your name: ")
        i = int(input("Enter your ID: "))
        y = input("Enter the name of book you want to issue: ")
        y = y.lower()
        l.issue(x,i,y)
    if n==3:
        x = input("Enter your name: ")
        i = int(input("Enter your ID: "))
        y = input("Enter the name of book you want to return: ")
        y = y.lower()
        l.return_book(x,i,y)
    if n==4:
        l.book_hol()
    if n==5:
        print("Thanks")
        break
    
