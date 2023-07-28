class Liabrary:
    no_of_books=0
    books=[]
    def check(self):
        if(len(self.books)!=self.no_of_books):
            print("Something went wrong")
            quit()
        else:
            print("Book added sucessfully")
    def add_book(self):
        b=input("Enter name of the which you want to add")
        self.books.append(b)
        self.no_of_books+=1
    def showinfo(self):
        print(f"{self.no_of_books} books available in liabray \nBooks are:")
        for i in range(len(self.books)):
            print(self.books[i],end=", ")
        print("\n")
a=Liabrary()
while True:
    c=int(input("Enter :\n 1 : for addbook\n 2 : Check for availability\n 3 : for Exit\n"))
    if(c==1):
        a.add_book()
        a.check()
    elif(c==2):
        a.showinfo()
    elif(c==3):
        print("Programm end")
        break
    else:
        print("Wrong choice")