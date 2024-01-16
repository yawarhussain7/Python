#Break and  COntinous Statement  

num = int(input("Enter the number : "))
print("Using For loop")
for i in range(12):
    if(i == 4):
        print("Skip the ilteration ")
        continue        # skip the current interation of the loop
    print(num," x ", i+1 ," = ",num* (i+1))

  
print("Using While loop ")  

num1 = int(input("Enter the another number : "))

i = 0;

while(i <= 12):
    print(num1," x ",i+1, " = ",num1 * (i + 1))
    if(i == 5):
        print("Break the loop ")
        break
    i +=1

print("While loop terminate ")

print("For loop start ")
for i in range(0,20,2):
    print(i)

print("This is another for loop ")

for i in [1,2,3,4,5,6,7,8,9,10]:
    if(i %2 != 0):
        continue
    print(i)


print("Try to create Do While loop ")
# create a do while loop 
i = 0
while True:
    print(i)
    i = i + 1
    if(i %100 == 0):
        break