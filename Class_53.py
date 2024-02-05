print("Topic: Mapping in Python ")

print("<<<<<<<<<< MAP In Python >>>>>>>>>>>")

def cube(x):
    return x * x * x

#find the cube of each element in the list and also written in list form

#   << Method 1
l = [1,2,4,6,8,3,6]

# newlist = []
# for i in l:
#     newlist.append(cube(i))
# print(newlist)

#   << Method 2

newl = list(map(cube,l))
print(newl)

# << Method 3


print("<<<<<<<<<<< FILTER In Python >>>>>>>>>>>>")
def filter_function(value):
    return value >= 40

marks = [12,23,34,45,56,67,78,89,90,88,44,93,54]

# we need to convert the filter() into list 
print(list(filter(filter_function,marks)))


print("<<<<<<<<<<< Reduce In Python >>>>>>>>>>>>")

from functools import reduce
# get sum of all the list 
testcase = [1,2,3,4,5,6,7,8,9]

print(reduce(lambda x,y: x + y,testcase))