print("Topic KBC Solution")




Questions = [

    ["Which language is use for automation of work ","C","C++","Python","Java","None",3],

    ["Which of the following is use to create website structure ? ","HTML","CSS","Python","JavaScript",3],

    ["Which of the following is use to Design & Styling the website ","HTML","XML","CSS","Python","None",3],

    ["Djongo is a ?","Framework","Programming Language","Application","None",3],
    
    ["Which of the following language are OOPs ?","Java","C++","Both","HTML","None",3],
    ["Which language is use for automation of work ","C","C++","Python","Java","None",3],

    ["Which of the following is use to create website structure ? ","HTML","CSS","Python","JavaScript",3],

    ["Which of the following is use to Design & Styling the website ","HTML","XML","CSS","Python","None",3],

    ["Djongo is a ?","Framework","Programming Language","Application","None",3],
    
    ["Which of the following language are OOPs ?","Java","C++","Both","HTML","None",3],

    ["Which language is use for automation of work ","C","C++","Python","Java","None",3],

    ["Which of the following is use to create website structure ? ","HTML","CSS","Python","JavaScript",3],

    ["Which of the following is use to Design & Styling the website ","HTML","XML","CSS","Python","None",3],

    ["Djongo is a ?","Framework","Programming Language","Application","None",3],
    
    ["Which of the following language are OOPs ?","Java","C++","Both","HTML","None",3],
    ["Which language is use for automation of work ","C","C++","Python","Java","None",3],

    ["Which of the following is use to create website structure ? ","HTML","CSS","Python","JavaScript",3],

    ["Which of the following is use to Design & Styling the website ","HTML","XML","CSS","Python","None",3],

    ["Djongo is a ?","Framework","Programming Language","Application","None",3],
    
    ["Which of the following language are OOPs ?","Java","C++","Both","HTML","None",3]

]

level = [1000,2000,3000,4000,5000,9000,13000,16000,20000,25000,30000,40000,50000]
money = 0
for i in range(0,len(Questions)):
    Question = Questions[i]
    print(Questions[i])
    print(f"Level {i} for {level[i]} Ruppes\n")
    print(f"a. {Questions[i][1]}       b.{Questions[i][2]}")
    print(f"c. {Questions[i][3]}       d.{Questions[i][4]}")
 
    replay = int(input("Enter your chooice... "))

    if(replay == Question[-1]):
        print(f"Correct Answer...! You have own {level[i]} Money")
        print(f"\nYour Current Balance is : {money}")
        money = level
    elif(i == 4):
        print(f"Congartualtion you have won Bouns Package {10000} Ruppes")
        print(f"\nYour Current Balance is : {money}")
        money +=10000
    else:
        print("Wrong Answer...! Nice try ")
        print(f"\nYour Current Balance is : {money}")
        money
    
        
    