# import module 
import pandas as pd

#import specfic function of the module 
from math import sqrt,pi


print(pd.__version__)

#to import specfic function we skip the module name 
print(sqrt(25))
print("The value of PI is : ",pi)

print("Topic : How import work in Python ")

# show all the function in the module 
import math
print("\n Math module function \n")
print(dir(math))

# print the function 
print(math.nan,type(math.nan))

#presonal Module
print("\nPersonal Modules ")
import C_44 as presonal

print(dir(presonal))
print(presonal.name)
print(presonal.hi())

