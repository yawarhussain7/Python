print("Topic : Exercise change the ramdom png file name in proper name")
import os
"""
Exampel

rad.png -> Pic1.png
exe.png -> Pic2.png
full.png -> Pic3.png
"""
# show all the images as the list form 
file = os.listdir("/media/dark/USBNTFS/FinalProject/Python/Images")
print(file)


i = 0
for img in file:
    if(img.endswith(".jpg")):
        os.rename(f"/media/dark/USBNTFS/FinalProject/Python/Images/{img}",f"/media/dark/USBNTFS/FinalProject/Python/Images/{i}.jpg")
        print(img)
    i = i +1
