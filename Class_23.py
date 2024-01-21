print("List Method in Python ")

List = [34,5,73,1,7,83]

print(List)

# append : this function insert a value at the end of list 
List.append(100)
print(List)

# sort: this function sort the unorder list  
List.sort()
print(List)

#sort(reverse=True): this function sort the list in decending order 
List.sort(reverse=True)
print(List)

#Reverse(): This function reverse the list not the order 
List.reverse()
print(List)

""" 
list1 = List
list1[0] = 444      This effect both of the list due to "Call by Reference concept " 
print(List)
                    Therefore we use the <copy() function
"""

list1 = List.copy()
print("\n")
print(List)
list1[0] = 555
print(list1)

print(list1 + List)
list1.extend(List)
print(list1)

list1.insert(0,999)
print(list1)