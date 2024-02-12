print("Topic: Super keyword for Constructor")

class Employee:

    def __init__(self,name,id):
        self.name = name
        self.id = id

class Programmer(Employee):

    def __init__(self,name,id,lang):
        super().__init__( name,id)
        self.lang = lang
        # self.name = name
        # self.id = id


Shoaib = Employee("Shoaib",136)
print(Shoaib.name)

Yawar = Programmer("Yawar",122,"Python")
print(Yawar.name)
print(Yawar.id)
print(Yawar.lang)

