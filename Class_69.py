print("Topic: Class Method")

class Company:

    company = "Google"
    
    def show(self):
        print(f"Employee name is {self.name}\n Company name is : {self.company}")
    

    @classmethod    # help to change the class variable 
    def change(self,new_comp):
        
        self.company = new_comp # it change the class variable 
    
c1 = Company()

c1.name = "Yawar "
c1.show()
c1.change("Infinity_tech")
c1.show()
print(c1.company)
    