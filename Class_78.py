print("Topic: Single Inheritance ")

class Animals:

    def __init__(self,animal,species):
        self.animal = animal
        self.species = species

    def make_sound(self):
        print("Make the sound of the animals ")


class Dog(Animals):

    def __init__(self,name,bearck):

        Animals.__init__(self,name,species="Dog")
        self.bearck = bearck
    
    def make_sound(self):
        print("breack")


d = Dog("Dog","Doging")
d.make_sound()

a = Animals("Dog","Bark")
a.make_sound()