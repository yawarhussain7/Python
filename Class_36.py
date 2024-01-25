print("Topic : Exception Handling in python ")
 

a = input("Enter the number : ")

print(f"The Multiplication table of {a} is : ")
try:
    for i in range(1,11):
       print(f"{int(a)} x {int(i)} = {int(a) * i}")

except Exception as Error:
    print("Invalid input \n",Error)
print("Improtant point ")
print("End of the program ")

#Value Error in Python
try:
    x = int(input("Enter the integer value "))
    a = [2,1]
    print(a[x])
   
except ValueError:
    print("Please input Integer value ")

except IndexError:
    print("Index Error ")

print("Program Terminate ")
