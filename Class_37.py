print("Topic : Finally Keyword in python")

def check():
    try:
        l = [2,3,5,6]
        x = int(input("Enter the index "))
        print(f"The value at index {x}  is {l[x]}")
        return 1
    except IndexError:
        print("Index Error found ")
        return 0
    finally:
        print("Program Terminated ") # always execute 

    print("It will not execute ") #program return value on the 1st step or 2nd step

y = check()
print(y)
