print("Topic Enumerate Function in python ")
#Enumerate function give the indexs of each element in list 

marks = [2,35,76,87,32,45,90,98,4,67,21]

print("With out using Enumeration Function ")

index = 0               
for i in marks:
    print(i)
    if(index == 7):
        print("Outstanding marks")
    index += 1

print("\n\b")
print("Same function with Enumeration")

for index,i in enumerate(marks):
    print(i)
    if(index == 7):
        print("Outstaind ")

# Example with stirng 
        
fruits = ["Apple","Banana","Mango"]

for index,i in enumerate(fruits,start=2):
    print(index,i)
    if(i == "Banana"):
        print(index,i,"Capture")
