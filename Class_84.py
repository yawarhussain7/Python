print("Topic: Time Module in python")

import time

def usingwhile():
    i = 0
    while(i < 500):
        print(i)
        i += 1


def usingfor():
    for i in range(501):
        print(i)

init = time.time()
usingwhile()
print(time.time() - init)

init = time.time()
usingfor()
print(time.time() - init)
print("wating for 3 second ")
time.sleep(3)

l = time.localtime()
local_Time = time.strftime("%Y-%m-%d-%H:%M:%S\n",l)
print(local_Time)
print("Now good bey ")
