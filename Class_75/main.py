print("Topic: Exercise")

#  You have give the random name jpg image 

# create a program that change each jpg images 
# and give proper name for each images

# Example: 

# adsdd.jpg   --> 1.jpg
# sed.jpg     --> 2.jpg
# 321s.jpg    --> 3.jpg

# Hint:   Use OS module

import os

files = os.listdir("/media/dark/USBNTFS/FinalProject/Python/Python/Class_75")
# print(files)
i = 0
for file in files:
    if(file.endswith(".jpg")):
        os.rename(f"/media/dark/USBNTFS/FinalProject/Python/Python/Class_75/{file}",f"/media/dark/USBNTFS/FinalProject/Python/Python/Class_75/image{i}.jpg")
    print(file) 
    i = i +1

