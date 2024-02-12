print("Topic: dir(), __dict__(),help()")

x = [12,23,34,45]
# show all the function which is applied on the list 
print(dir(x))
# show detail of the function
print(x.insert)


class Person:

    def __init__(self,name,id):
        self.name = name
        self.id = id
    
print('\n')
p = Person("Yawar HUssain",122)

# dict give the user define function and method of the class
print(p.__dict__)
# help give complete information 
print("\n",help(Person))
