print("Topic: Multi-Level Inheritance")

class Animal:

    def __init__(self,name,species):
        self.name = name 
        self.species = species

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
    
class Dog(Animal):

    def __init__(self,name,breed):
        Animal.__init__(name,species="Dog")
        self.breed = breed
    
    def show_details(self):
        Animal.show_details(self)
         

class GoldenTetriver(Dog):

    def __init__(self,name,color):
        Dog.__init__(self,name,breed="Golden Retriever")
        self.color = color

    def show_details(self):
        Dog.show_details(self)
        print(f"Color : {self.color}")


G = GoldenTetriver("TOmmy","Black")
G.show_details()