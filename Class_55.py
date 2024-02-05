import random

def Game(a,b):
    if(a==b):
        return 0
    
    elif(a == 0 and b == 1):
        return -1
    elif(a == 1 and b == 2 ):
        return -1
    elif(a == 2 and b == 0):
        return -1
    
    return 1

print("Topic: Snake, water & Gun")

scoure = 0
chance = 5
while(chance >= 0):

    print("0 => Press for Snake\n 1 => Press for Water\n 2 => Press for Gun")

    comp = random.randint(0,2)
    print(comp)
    usr = int(input("Chooice your option (0 - 2) : "))

    G = Game(comp,usr)
    chance -=1
    if(G == 1):
        print("User won ")
        scoure += 100
        print("\n")
        print("Your Scoure is : ",scoure)
    elif(G == -1):
        print("Computer won ")
        print("\n")
        print("Your Scoure is : ",scoure)
    else:
        print("Game Draw")

print("Your total source is : ",600)
print("You have obtain : ",scoure)