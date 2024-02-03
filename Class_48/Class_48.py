
print("******** Read File *********")


# f = open('/media/dark/USBNTFS/FinalProject/Python/Python/Class_48/info.txt')  read is default mode in File Handling therefor we use read file like this
f = open('/media/dark/USBNTFS/FinalProject/Python/Python/Class_48/info.txt','r')
# print(f)  not give content of the txt
text = f.read()
print(text)

f.close()

# for binary file  read 
# f = open ('file_name.txt','rb')

# for text file read 
# f = open('file_name.txt','rt')

print("********* Write File **************")

f1 = open("/media/dark/USBNTFS/FinalProject/Python/Python/Class_48/write.txt","w")

f1.write("Hello THis is my first File handling program in python ")

f1.close()

print("********* Append File **************")

f2 = open("/media/dark/USBNTFS/FinalProject/Python/Python/Class_48/append.txt","a")

f2.write("Hello this is append function ")

f2.close()