print("Topic: seek() & and tell()  trancate() method in Python")

with open('/media/dark/USBNTFS/FinalProject/Python/Python/Class_51/file.txt','r') as f:
    print(type(f))
    #skip the character at the starting
    f.seek(10)
    # display current location in the file.txt 
    print(f.tell())

    # read 20 lines and store in line variable 
    line = f.read(20)
    # display to user 
    print(line)

#write file 
with open('/media/dark/USBNTFS/FinalProject/Python/Python/Class_51/newfile.txt','w') as f1:
    #writing in the file 
    f1.write("Hello This is file handing program in python ")
    # specify the writhing character (only five charcter will store in the file)
    f1.truncate(5)

#read file
with open('/media/dark/USBNTFS/FinalProject/Python/Python/Class_51/newfile.txt','r') as f1:
    
    print(f1.read())


