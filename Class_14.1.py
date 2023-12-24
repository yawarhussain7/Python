print("Nested IF ELIF Statement")

num1 = int(input("Enter the value of num1 : "))
num2 = int(input("Enter the value of num2 : "))
num3 = int(input("Enter the value of num3 : "))

if(num1 > num2):
    if(num1 > num3):
        print(num1," is a greatest number ")
elif(num2 > num1 ):
    if(num2 > num3):
        print(num2," is greatest number")
else:
    print(num3," is greatest number")

print("Programm is successfully compile ")