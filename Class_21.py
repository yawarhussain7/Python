

# average function 
def average(a = 3,b = 2):

    avg = (a + b)/2
    print("Average is : ",avg)
average()       #default 
print("\n")
average(4,6)    # it over write the local variable of funtion 
print("\n")


# hello function 
def hello(first = "Yawar ",last="Hussain"):
    print("Hello ",first," ",last)

print("This is Default argument ")
hello()

print("\n");
print("This is Required argument ") 
# You must give argument in order 
hello(first="Imran")
print("\n");

# keyword argument 
# in this you can change the place of argument 
print("This is Keyword argument")
hello(last = "Hussain",first = "Muhammad ")
print("\n");


# function with tuple 

def newavg(*num):       # *num is a tuple which contain collection of number 
    print(type(num))
    sum = 0
    for index in num:
        sum = sum + index
    avg = sum / len(num)
    print("New Average is : ",avg)

newavg(5,6)
print("\n")
newavg(2,3,5,7,80,43,12,3,5,6)
print("\n")

# function with dictionary 

def name(**name):
    print(type(name))
    print("Hello ",name["fname"],name["lname"])



name(fname= "Yawar ",lname = "Hussain")
