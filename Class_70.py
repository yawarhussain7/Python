print("Topic: Class method as Altirbute ")

class Emp:

    def __init__(self,name,salary):
        self.name = name
        self.salary = int(salary)

    @classmethod
    def fromstr(cls,str):
        return cls(str.split("-")[0],int(str.split("-")[1]))
    
E1 = Emp("Yawar",12333)
print(E1.name)
print(E1.salary)

str = "Hussain-125555"
# E2 = Emp(str.split("-")[0],str.split("-")[1])
E2 = Emp.fromstr(str)

print(E2.name)
print(E2.salary)
