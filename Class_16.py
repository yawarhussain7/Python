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
