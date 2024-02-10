print("Topic : Instance Variable Vs CLass Variable \n")
"""
Class Variable is applied for all the class and its object 

eg -> Company name is same for all the employee who working in the company 

Instance Variable is applied for specfic Object 

eg -> Every worker have different rank and salary in the same company
"""
class Employee:

    #class variable
    company = "Infinity_Tech"

    total_emp  = 0


    def __init__(self,name):
        self.name = name
        self.bounus = 0.2
        
        Employee.total_emp += 1     # Class variable 


    def show(self):
        print(f"The name of Employee is : {self.name}")
        print(f"The Bonus amount of Employee in {self.company} is : ${self.bounus}%")
        print(f"Your Position is : {self.total_emp}\n")


emp1 = Employee("Yawar Hussain")

#both do same thing 
# emp1.show()
# Employee.show(emp1)

emp1.show()

emp2 = Employee("Muhammad Hussain")
emp2.company = "Google"
emp2.bounus = 0.3
emp2.show()

print(Employee.company)