print("Topic: Library Management System ")

class Library:

    def __init__ (self):
        self.BookNo = 0
        self.Books = []

    def addBook(self):
        
        book = input("Enter the book name : ")
        self.Books.append(book)
        self.BookNo = len(self.Books)
    
    def show(self):
        
        for book in self.Books:
            print(book)
        
        print(f"The Book number is : {self.BookNo}")


l = Library()

l.addBook()
l.addBook()
l.show()