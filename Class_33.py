print("Topic : Dictionary in Python ")

marks = {
    "Programming": 46,
    "Software":70,
    "Physics":81,
    "Pakistan Studies":70
}

print(marks["Programming"])
print(marks)
print(marks.keys())
print(marks.values())

for i in marks:
    print(f"{i} = {marks[i]}")

info = {
    "Name":"Yawar Hussain", 
    "age":20,
    "Height":5.4,
    "weight":57
}

print(info.items())

for key,value in info.items():
    print(f"{key} : {value}")