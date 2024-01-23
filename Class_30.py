"""
    fact(5) = 5 x 4 x 3 x 2 x 1 = 120
    fact(4) = 4 x 3 x 2 x 1
    fact(3) = 3 x 2 x 1
    fact(2) = 2 x 1 
    fact(1) = 1
"""

print("Topic:\n Recursion in Python ")

print("Factorial Example \n")

def Recursion(a):
    if(a == 0 ):
        return 1
    elif(a == 1):
        return 1
    else:
        return a*Recursion(a - 1);

a = int(input("Enter a number "))
print(f"Factorial of {a} = ",Recursion(a))

# Dry run 

"""
let the value of a is 5 

a = 5 

5 * Recursion(5-1) = 5 * Recursion(4) :     return 5 * 25 = 120

4 * Recursion(4-1) = 4 * Recursion(3) :     return 4 * 6 = 24

3 * Recursion(3-1) = 2 * Recursion(2) :     return 3 * 2 = 6

2 * Recursion(2-1) = 1 * Recursion(1) :     return 2 * 1 = 2
"""

print("Fibonacci Example \n")

def fibo(a):
    if(a == 1):
        return 0
    if(a == 2):
        return 1
    else:
        first = fibo(a - 1)
        second = fibo(a - 2)
        return first + second


num = int(input("Enter a Positive number : "))

print(f"Fiboncci of {num} term is : ",fibo(num))

# Dry Run

"""
    let num =  5 

    <<<<<<<< First >>>>>>>>>
    first = fibo(5 - 1) = 4             : return 3
        first = fibo(4 - 1) = 3         : return 2

    <<<<<<<< Second >>>>>>>>>
    second = fibo(5 - 2) = 3             : return 3
        second = fibo(3 - 2) = 1         : return 1
        

    return : 1 + 2      ans = 3
"""