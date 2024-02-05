print("Topic: = Vs == ")

num = 4
str = "4"

print("using is : ",num is str) # campare location in the memory 
print("using == : ",num == str) # campare value of variable 


# Give correct answer because values are immutable 
num = 4
str = 4
print("using is : ",num is str) # campare location in the memory 
print("using == : ",num == str) # campare value of variable 

tup1 = (3,4)
tup2 = (3,4)
print("using is : ",tup1 is tup2)
print("using == : ",tup1 == tup2)

val = None
print("using is : ",val is None)
print("using == : ",val == None)