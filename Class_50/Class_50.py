print("<=========== Read from file ===========>")
f = open("/media/dark/USBNTFS/FinalProject/Python/Python/Class_50/file.txt","r") 
while True:
    line =  f.readline()
    print(line)
    if not line:
        print(type(line))
        break


print("<<<<<<<< Reading marks >>>>>>>>>>>>")
marks = open("/media/dark/USBNTFS/FinalProject/Python/Python/Class_50/marks.txt","r") 

i = 0

while True:
    i = i + 1
    line = marks.readline()

    if not line :
        break
    
    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])

    print(f"The Math marks of student {i} is {m1}")
    print(f"The English marks of student {i} is {m2}")
    print(f"The Urdu marks of student {i} is {m3}")

    print(line)


print("<<<<<<<<< Write in File >>>>>>>>>>>")

file = open("/media/dark/USBNTFS/FinalProject/Python/Python/Class_50/write.txt","w")

line = ["ALi: Hi Sana how are your ?\n","Sana: I am good thank you what's about you ALi?\n"]
file.writelines(line)

file.close()
