print("Get input from user ")

num1 = input("Enter the value of num1 : ")
num2 = input("Enter the value of num2 : ")

print(num1," + ",num2, " = ",num1 + num2)
# it will concatinate the both number 
# By default the  the input function have string value 

#if we add two number then first we need to typecast string to integer 

print(int(num1), " + ",int(num2)," = ",num1 + num2)
# it also concatinate the value because we convert both number but we cannot convert it result 

# print(num1," / ",num2, " = ",int(num1 / num2))
# it will give ERROR because int( num1 / num2 ) first it add number then call the int() function
# in over case both number are string 

print("******* Operation *************")
print(num1," / ",num2, " = ",int(num1) / int(num2))
print(num1," % ",num2, " = ",int(num1) % int(num2))     #Give reminder
print(num1," // ",num2, " = ",int(num1) //int( num2))   #remove digits after point
print(num1," * ",num2, " = ",int(num1) * int(num2))
print(num1," + ",num2, " = ",int(num1) + int(num2))
print(num1," - ",num2, " = ",int(num1) - int(num2))
print(num1," ** ",num2, " = ",int(num1) **int( num2))   # pow function first number the power
