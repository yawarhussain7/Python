# Function is a block of a statement which performed specfic task 
# there are two type of function 
    # 1. User define function       which are define by user 

    #Example : 

        #  def sum(a,b):
            # print(a, " + ", b , " = ", a + b)

    # 2. Build in function          which is pre install with compliler 

    # Example :

        # print(), int() and input() etc...



# find the greatest number 
def large(a,b):
    if(a > b ):
        print(a,"   is greatest number ")
    elif(a == b):
        print(a," & ",b,"   are equal ")
    else:
        print(b,"   is greatest number ")

# find the less number 
def less(a,b):
    pass                # it tell that i will define it letter you may complete your task 

#find the sum of two number
def sum(a,b):
    sum = a + b;
    print(a ," + ", b ," = ", sum)
    print("\n")
    large(a,b)  # invoking largest funtion 

# find Geomatric mean 
def Gemo(a,b):
    mean = ( a * b ) / ( a + b )
    print("Geomatric Mean is : ",mean)


a = 4;
b = 2;
# sum1 = a + b;         with out using function we calculate with different variable or print 
# print(sum1)            for each statement 

sum(a,b)                #Doing same thing 
print("\n")
Gemo(a,b)               #find Geomatric mean
print("\n")

c = 6
d = 9
# sum2 = c + d              to avoid this we use function 
# print(sum2)

sum(c,d) 
print("\n")
Gemo(c,d)       #find Geomatic mean
print("\n")

