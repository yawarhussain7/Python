print("Topic: Local & Global Variable ")

x = 45
print(x)

def hello():
    global x # global variable use 
    x = 33      #modify global variable 
    print(f"The local variable is : {x}")   
    y = 12
    print("Hello Yawar Bahi")
    print(f"The value of y is : {y}")

print(f"The global variable is : {x}")      
#invoked function
hello()
#global variable is changed when function invoked
print(f"The global variable is : {x}")

# print(f"THe value of Y is : {y}") it will give error because y is accessible with in the funtion 