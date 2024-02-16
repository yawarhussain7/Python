print("Topic: Hybrid & Herarcial Inheritance ")

print("<<== Hybrid Inheritance ==>>")

class Base:
    
    def __init__(self,name):
        self.name = name

    def show(self):
        print(f"Name : {self.name}")


class Derived_01(Base):
    
    # def __init__(self,id):
    #     Base.__init__(self,name= "Yawar")
    def __init__(self, name, id):
            super().__init__(name)
            self.id = id
    
    def show(self):
        Base.show(self)
        print(f"ID : {self.id}")


class Derived_02(Base):
    
    # def __init__(self,id):
    #     Base.__init__(self,name= "Yawar")
    def __init__(self, name, salary):
            super().__init__(name)
            self.salary = salary
    
    def show(self):
        print(f"Salary : {self.salary}")

d = Derived_02("Yawar",122)
d.show()

