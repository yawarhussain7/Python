# create a program which convert massage int screate message 


""" code => edoc

    Rules for Encrypt:
    1-  if a massage contain atleast 3 character remove 1st letter and append it at the end 
    2-  append 3 random character at the starting and ending of the massage 
    3-  Else reverse the massage 

    Rule for Decrypt:
    1- remove the string and ending 3 character 
    2- remove the last character and append it at the sarting
    2- Else reverse the massage


"""
#get input massage from the user 
str = input("Enter your massage : ")
# break down the stirng into small parts
words = str.split(" ")
# give chooice for user 
coding = input("1 => Press for Encrypt \n0 => Press for De-crypt.... ")

coding = True if(coding == "1") else False
print(coding)

if(coding):
    #ceate empty stirng 
    nwords = []

    for word in words:
        #calculate the len of the string 
        if(len(word)>=3):
            #get random character 
            r1 = "dsr"
            r2 = "sod"
            # stnew variable create and store encrypted code
            stnew = r1 + word[1:] + word[0] + r2

            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    # again create empty string 
    nwords = []

    for word in words:
        #find the length of the string 
        if(len(word)>= 3):

            stnew= word[3:-3]           
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))