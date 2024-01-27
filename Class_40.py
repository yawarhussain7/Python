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

massage = input("Enter your massage : ")

line = int(len(massage))

massage1 = massage

if(line < 3):
    massage1 = massage[1]+massage[0]
    
else:
    random1="kid"
    random2="fit"
    for i in range(0,line):
        massage1 = massage[i+1]
    


print(f"Massage = {massage}")
print(f"Massage1 = {massage1}")