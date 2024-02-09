print("Topic: Getter and Setters in Python ")

class MyClass:
    
    def __init__(self,value):

        self._value = value
    
    def show(self):
        print(f"Value is {self._value}")
    
    #Getter 
    @property
    def ten_value(self):
        return 10 * self._value
    #Setter
    @ten_value.setter
    def ten_value(self,new_value):
        self_value= new_value/10


obj = MyClass(10)
# obj.ten_value = 57  Give error we cannot chage the value of object like this we need to use setter 
obj.ten_value = 67
print(obj.ten_value)
obj.show()
