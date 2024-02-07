print("Topic: Decorators in Python ")

print("\n<<===== Example 1 ======>>")
# decorator get a function from user and return after update the function or modify some chanage 


#Declearing Decorator function
def thnk(hello):
    # without any argument
    def system():

        print("Thank you for using Over service ")
        hello()
        print("Enjoy you Trip ")
    
    # return system function after modify 
    return system

#invoking Decorate function
@thnk
def hello():
    print("Hello world")


hello()

print("<<===== Example 2 ======>>")

def decorator_function(fx):
    #sum(tuple , dictionary)    as argument 
    def sum(*tup,**dec):
        print("Welcome ")
        fx(*tup,**dec)
        print("Thank you for using over service")
        
    return sum


@decorator_function
def add(a,b):
    print(a+b)

add(3,4)
