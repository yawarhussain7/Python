# create a program which convert massage int screate message 


""" code => edoc

    Rules for Encrypt:
    1-  if a massage contain atleast 3 character remove 1st letter and append it at the end 
    2-  append 3 random character at the starting and ending of the massage 
    3 - Else reverse the massage 

    Rule for Decrypt:
    1- remove the string and ending 3 character 
    2- remove the last character and append it at the sarting
    2- Else reverse the massage


"""
print("Encrypting Process ")
massage = input("Enter your massage : ")

line = len(massage)

# massage1

if(line < 3):
    massage1 = massage[1:]+massage[0]
    print(f"Massage1 = {massage1}")

elif(line > 3):
    random1 = input("Input 3 Random Character : ")
    random2 = input("Again Input 3 Random Character : ")
    massage =  random1 + massage[1:] + massage[0] + random2

else:
    print(ValueError("ERROR both case are woring "))

print(f"Massage = {massage}")
    





print("\n\nDecrypting Process....")

