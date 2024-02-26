from functools import lru_cache
# use when we are working specfic value 
# it will give result ripdly

import time

print("Topic: Function Caching ")

@lru_cache(maxsize=None)

def fx(n):
    time.sleep(5)
    return n*5

print(fx(20))
print("DOne for 20")

print(fx(4))
print("Done for 4")

print(fx(2))
print("Done for 2")

# it print immidiatily because lru_cache store previous value 
# when we re run the program the cache will again empty 

print(fx(20))
print("DOne for 20")

print(fx(4))
print("Done for 4")

print(fx(2))
print("Done for 2")

# it will take more time because it does not store in cache 
print(fx(32))
print("DOen for 32")
