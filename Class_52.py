print("Topic: Lamda function in Python ")

#define sum function
def sum(a,b):
    return a + b
# display output 
print(sum(2,3))

#define add function with lamda 
add = lambda a,b: a + b
print(add(3,6))
#define cube
cube = lambda a: a*a*a
print(cube(5))
#define avg 
avg = lambda x,y: (x + y)/2
print(avg(3,4))


#function as arguments 
def apply(fx,value):

    return 2 + fx(value)

print("Apply = ",apply(cube,2))
print("New anonmous function : ",apply(lambda x: x * x,5))
