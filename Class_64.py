print("Topic : Library Management system \n")

class Library:

    def __init__(self):
        self.NoBook = 0
        self.books = []
    
    def add(self,book):
        self.books.append(book)
        self.NoBook = len(self.books)
    
    def show(self):
        for book in self.books:
            print(book)
        print(f"The numebr of books is : {self.NoBook}\n")

L1 = Library()

L1.add("Kali_linux")

L1.show()

L1.add("Networking")

L1.show()