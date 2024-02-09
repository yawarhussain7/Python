import random
print("Topic: SImpel Game ")

def Game(a,b):
    if(a == b):
        return -1

    elif(a == 0 and b == 2):
        return 0
    elif(a == 1 and b == 0):
        return 0
    elif(a == 2 and b == 1):
        return 0
    else:
        return 1

score = 0
change = 5
while(True):
    print(f"\n\t Chance {change}")
    print("\n [0] press for Snake\n [1] press for water \n [2] press for Gun")

    comp = random.randint(0,2)

    human = int(input("Chooice....."))

    result =  Game(human,comp)

    if(result == 0):
        print("Computer won")
        print(f"Points : {score}")
    elif(result == -1):
        print("Match Draw")
        print(f"Points : {score}")
    else:
        print("Human Own")
        score += 100
        print(f"Points : {score}")

    print(f"\tComputer Chooice :  {comp}")
    change -= 1
    if(change == 0):
        break