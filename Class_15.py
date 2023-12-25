import time
second = time.time()
print("Second is : ",second)

local_time  = time.ctime(second)        #print local time as human readable form
print("Local time is : ",local_time)

print("It it print immidiately")
sleep = time.sleep(3)
print("It it print after 3 second ")    # it will take 3 second for print in termainal 
time.sleep(3)   
print("It it print after more 3 second")


# Exe 
# create a program that say Good Morning and Good night according to Local time 

Hours =int( time.strftime("%H"))
print(Hours)

min = int(time.strftime("%M"))
print(min)

sec = int(time.strftime("%S"))
print(sec)

if(Hours >= 8  and Hours <= 12):
    print("Good Morning")
    if(Hours >= 1 ):
        Hours = 13;
elif(Hours >= 12 and Hours <= 17):
    print("Good After noon")

elif(Hours >= 18 and Hours <= 24):
    print("Good Night")
