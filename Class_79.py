print("Topic: Multiple Inheritance ")

class Employee:

    def __init__(self,name):
        self.name = name
    
    def show(self):
        print(f"Name : {self.name}")
    

class Artist(Employee):

    def __init__(self,art):
        self.art = art
    
    def show(self):
        print(f"Art : {self.art}")


class Programmer(Artist,Employee):

    def __init__(self,name,art):

        self.name = name
        self.art = art


P1 = Programmer("Yawar","Pencil Skeches")
# print(P1)
print(P1.name)
print(P1.art)
P1.show()

# show the finding order of the class 
print(Programmer.mro())