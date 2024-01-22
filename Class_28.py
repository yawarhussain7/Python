print("String formating in Python ")

letter = "My name is {} and I am from {}"

name = "Yawar"
country = "Pakistan"

print(letter.format(name,country))

letter = "My name is {1} and I am from {0}"
print(letter.format(country,name))

print(f"My name is {name} & i am from {country}")

num = 32.432323
print(f"You have {num:.2f} Dollar")

print(f"{2 * 19}")


# show syntax 
print(f" f-string is written like this \n My name is {{name}} & i am from {{country}}")