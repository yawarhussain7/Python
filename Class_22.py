print("Topic \n List in Python ")

sub_marks = [34,33,39,41,56,76,87,98,65]
print(sub_marks)
print(type(sub_marks))

print("List printing Method \n")

print("Print using index of list ")
print(sub_marks[0])
print(sub_marks[1])
print(sub_marks[2])
print(sub_marks[3])

print("Control indexs ")
print(sub_marks[1:3])       # print form 1 index to 3 index 
print(sub_marks[:])         #print form 0 index to last index
print(sub_marks[1:6:2])     #print form 1 index to 6 index with jump 1 index

# in Operation : we can use to search 
if(98 in sub_marks):
    print("Your Number is present")

else:
    print("Your Number is Not present ")

# Rondom list 

random = ["Yawar",4.34,32,True,None]
print(random)

print("\n")
print("Print Random list using Negative indexing ")
print(random[-3])
print(random[len(random) - 3])

print("\n")
print("Another list ")

another = [i for i in range(10)]
print(another)
print("update list ")
another = [i*i for i in range(10)]
print(another)

