import time

print("Exercise 2: Create a program which show massage according to local time \n ")
print("Say you \n Good Morning\n Good Evening\n Good Night")

hours = int(time.strftime("%H"))
print(hours)

if(hours >= 0 and hours <= 12):
    print("Good Morning sir")
elif(hours >= 12 and hours <= 17):
    print("Godd AfterNoon sir")
elif(hours >= 13 and hours < 0):
    print("Godd Night sir")
else:
    print("Invalid Operation")