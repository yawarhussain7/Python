print("String Method in Python ")

# string are immutable it mean it cannot change
name = "!!!!!Yawar!!!!!"
print(len(name))  # print the length of the string
print(name.upper())  #convert string to upper case
print(name.lower())  #convert string to lower case

print(name.rstrip("!"))  #remove ! symbol after the print
print(name.replace("Yawar", "Hussain"))  #replace Yawar with Hussain

channel = "COde WIth HarrY"
print(channel.capitalize(
))  #capitalize the first letter of the string and other letters are lower case

wel = "Welcome to Infinity Tech "
print(len(wel))
print(wel.center(50))  #give space in the middle of the string
print(wel.count("e"))  # count the number of e in the string

open = ">>> Welcome to COnsole <<<<"
print(open.startswith(">"))  #check if the string start with >
print(open.endswith("<"))  #check if the string end with <

mas = """
HI THis is Yawar Hussain 
Yawar Hussain is belong to Pakistan 

Yawar Hussain is a Python programmer 
Yawar Hussain Work on replit 
"""
print(mas.find("Yawar Hussain"))  # finde the index of Yawar Hussain
print(mas.index("Yawar Hussain"))
# print(mas.index("Muhamad ALi")) it will give error then exit the code because Muhamad ALi is not in the string

# A string which contain A-Z a-z 0-9  called alphanumarica string
alpnum = "012345AsidfFISIS"  #check the alpnumarica string
print(alpnum.isalnum())

alpha = "ABsceD"
print(alpha.isalpha())  #check the alpha string

printable = "   this is yar\n"
print(printable.isprintable())  # false due to \n

space = " "
print(space.isspace())  #check the wide spaces

title = "Introduction to Programming Fundamentals"
print(title.istitle())  #check the title string

print(title.swapcase())  # convert lower to upper and upper to lower
print(title.title())
#convert the text intot title
