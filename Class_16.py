print("Match statement in python ")

day  = input("Enter the day : ")

match day:
    case 'Monday':
        print("TOday is Monday")
    case 'Tuesday':
        print("Today is Tuesday")
    case 'Wednesday':
        print("Today is Wednesday")
    case 'Thursday':
        print("TOday is Thursday")
    case 'Friday':
        print("Today is Friday")
    case 'Saturday':
        print("Today is Saturday")
    case 'Sunday':
        print("Today is Sunday")
    case _ :
        print("Invalid input ")


x = int(input("Enter the number : "))

match x:
    case 10:
        print("Your number is : ",x)
    case 20:
        print("Your number is : ",x)
    case _ if x != 40:
        print("Your number is NOt equal to 40 \n Your number is ",x)    #default cases
    case _ if x > 60:
        print("Your number is Greater or Equal to 60 \n YOur number is ",x)
    case _ if x < 80:
        print("Your number is Less than 80 \n Your number is  ",x)
    case _ :
        print("Invalid input")
