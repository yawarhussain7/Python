total = int(5*20)
score  = int(0)

# Questions_01 
print("Question 1: CPU stand for ?\n ")
Questions_01 = [ 
         ["0 => Center Processing unit "],
         ["1 => Center Program Unit"],
         ["2 => Current Processing Unit"]
]

print(Questions_01[0])
print(Questions_01[1])
print(Questions_01[2])
chooice = int(input("Chooice ..."))

if(chooice == 0):
        print("Correct");
        score += 20
        print("Your Score is : ",score)

elif(chooice == 1 or chooice == 2):
        print("Wrong")
        print("Your Score is : ",score)
print("\n")
# Questions_02 
print("Question 1: RAMstand for ?\n ")
Questions_02 = [ 
         ["0 => Ruman Access Memory "],
         ["1 => Read Access Memory"],
         ["2 => Random Access Memory"]
]

print(Questions_02[0])
print(Questions_02[1])
print(Questions_02[2])
chooice = int(input("Chooice ..."))

if(chooice == 2):
        print("Correct");
        score += 20
        print("Your Score is : ",score)

elif(chooice == 1 or chooice == 0):
        print("Wrong")
        print("Your Score is : ",score)
print("\n")
# Questions_03 
print("Question 1: ROM stand for ?\n ")
Questions_03 = [ 
         ["0 => Ruman OrdanaryMemory "],
         ["1 => Read Only Memory"],
         ["2 => Random Only Manage"]
]

print(Questions_03[0])
print(Questions_03[1])
print(Questions_03[2])
chooice = int(input("Chooice ..."))

if(chooice == 1):
        print("Correct");
        score += 20
        print("Your Score is : ",score)

elif(chooice == 2 or chooice == 0):
        print("Wrong")
        print("Your Score is : ",score)

print("\n")
# Questions_04
print("Question 1: IP stand for ?\n ")
Questions_04 = [ 
         ["0 => Internet Present "],
         ["1 => Interface Protocol"],
         ["2 => Internet Protocol"]
]

print(Questions_04[0])
print(Questions_04[1])
print(Questions_04[2])
chooice = int(input("Chooice ..."))

if(chooice == 2):
        print("Correct");
        score += 20
        print("Your Score is : ",score)

elif(chooice == 1 or chooice == 0):
        print("Wrong")
        print("Your Score is : ",score)
print("\n")
# Questions_05
print("Question 1: SEOstand for ?\n ")
Questions_05 = [ 
         ["0 => Scan Engine Operation "],
         ["1 => Search Engine Optimization"],
         ["2 => Search Engine Operators"]
]

print(Questions_05[0])
print(Questions_05[1])
print(Questions_05[2])
chooice = int(input("Chooice ..."))

if(chooice == 1):
        print("Correct");
        score += 20
        print("Your Score is : ",score)

elif(chooice == 2 or chooice == 0):
        print("Wrong")
        print("Your Score is : ",score)
print("\n")

print("Total Number : ",total)
print("Your Score is : ",score)

if(total == score):
        print("Congartulation \n You have give all correct number")