print("TOpic : Custom Error in python")

x = int(input("Enter a value between 5 to 10 : "))

if(x < 5 or x > 10):
    raise ValueError("Your value is Invalid\n Please give value between 5 to 10")

else:
    print(x)


# Quiz: Create a program which does't show error when user give input "quick" other wise show error 
    
text = input("Enter a massage ")

if(text == "quick"):
    print(text)
else:
    raise NameError("Your massage is Wrong")


