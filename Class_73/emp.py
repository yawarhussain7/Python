class Employee:

    def __init__(self,name):
        self.name = name 

    def __len__(self):
        i = 0 
        for item in self.name:
            i = i + 1
            return i

    def __str__(self):
        return (f"The name of the Employee is : {self.name } using str")

    # if __str__ is not present then it work 
    def __repr__(self):
        return (f"The name of the Employee is : {self.name } using repr")

    def __call__(self):
        return ("Good Bey")