print("Topic: Constructor in Python ")

class Person:

# Constructor call when Class is invoked when object 
    
    #self is the by default parameter 
    def __init__(self,n,r):
        print("Welcome to Infinty Tech ")

        self.name = n
        self.role = r
    
    def info(self):
        print(f"{self.name} is a {self.role}")


a = Person("Yawar","Developer")
b = Person("Shoaib","Block Chain Developer")

a.info()
b.info()