print("Topic:   Generator in Python")


def my_Gen():
    
    for i in range(5):
        yield i


gen = my_Gen()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))  given Error because it is not include in for loop


print('\n')

for i in gen:
    print(i)