print("Topic: Access Modifier")

print("\n<<<=== Public Modifier ===>>>\n")

class Name:

    def __init__(self):
        # public 
        self.name = "Yawar Hussain"
        # private 
        self.__age = 21 
        


n1 = Name()
# Directly access
print(n1.name)
print("\n<<<=== Private Modifier ===>>>\n")

# print(n1.__age) Give an error 
print(n1._Name__age)

print(n1.__dir__())

print("\n<<<=== Protected Modifier ===>>>\n")

class Student:

    def __init__(self):

        self._name = "Yawar Hussain"
    
    def _funName(self):
        return "Good Bey "
#   Class Inherite
class Subject(Student):

        pass

obj = Student()
obj1 = Subject()

# calling by object of Student  class
print(obj._name)
print(obj._funName())
print("\n")
# calling object of Subject class
print(obj1._name)
print(obj1._funName())

