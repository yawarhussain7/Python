print("Topic: Super() keyword")

class Parent_Class:

    def Parent_Method(self):
        print("This is Parent class ")


class Child_Class(Parent_Class):

    def Parent_Method(self):
        print("Yawar Hussain")
        return super().Parent_Method()
    
    def Child_Method(self):
        print("This is Child class")


c = Child_Class()
c.Child_Method()
c.Parent_Method()