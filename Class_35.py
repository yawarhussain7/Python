print("Topic : For loop in Python")

for i in range(2):
    print(i)
else:
    print("Sorry value not found ")


for i in range(6):
    print(i)
    if( i == 4):
        break

else:
    print("404 Not found ")


print("\n")
i = 0


while i < 7:
    print(i)
    i += 1
    if(i == 5):
        break
else:
    print("For loop terminate ")