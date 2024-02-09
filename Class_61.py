print("Topic : Inheritance in Python")
#ase Class
class Employee:
    
    def __init__(self,name,id):

        self.name = name
        self.id = id

    def show(self):
        print(f"Employee name : {self.name}")
        print(f"Employee ID : {self.id}")

# Derived Class

class Programmer(Employee):

    def __init__(self,language):
        
        self.language = language
    
    def showdata(self):
        print(f"THe Programmer expert in {self.language}")



P1 = Employee("Yawar Hussain ",122)
P1.show()

P2 = Programmer("Python")
P2.showdata()

