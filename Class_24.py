print("Tuple in Python ")
# Tuple are immutable data type 

tup = (2,3,5,54,67,987)       # unchange-able
print(tup)
# tup[0]= 343       Give ERROR 
print(type(tup))

print("<<======= Indexing in Python ==========>>\n")
tup1 = ("yawar",34,5.43,True)

print(tup1[0])
print(tup1[1])
print(tup1[2])
print(tup1[3])
# print(tup1[34])       Give ERROR out of index 

print("<<======= Negative Indexing ==========>>\n")
print(tup1[len(tup1) - 2])
print(tup1[4-1])

if 34 in tup1:
    print("Yes number present")
else:
    print("Not Present")

print("<<======= String Slicing ==========>>\n")

tup2 = tup[1:]
print(tup2)
