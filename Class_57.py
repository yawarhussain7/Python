print("Topic : Classes & Objects in python ")

class person:
    name = "Yawar"
    role = "Programmer"

    def info(self):
        print(f"{self.name} is a {self.role}")


a = person()

# change the name and role 
a.name = "Hussain"
a.role = "Nurse"

# print(a.name,a.role)

a.info()

b = person()

b.name = "Abbas"
b.role = "Software Developer"

b.info()
# if we does't not modify the method it will give by defualt value which is define in class
c = person()
c.info()