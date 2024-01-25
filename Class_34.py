print("Topic : Dictionary method in python ")

info = {
    "Name":"Yawar",
    "age":20,
    "ID":122,
    "Dep":"Software Engineering",
    "Email":"y@awar76@gmail.com",
}

info_01 = {
    "Name1":"Hussain",
    "age1":23,
    "ID1":123,
    "Dep1":"CNA",
    "Email1":"hu$$ain@gamil.com"
}

info.update(info_01)
# print(info)
for key,value in info.items():
    print("\n")
    print(f"{key} = {value}")

#clear 
info.clear()
#empty dictionary
emp = {}
print(emp)
#pop 
infor = {1:100,2:101,3:102,4:103,5:104}
infor.pop(2)
print(infor)
# popitem : remove last items
infor.popitem()
print(infor)

#delete 
del infor[1]
print(infor)
del infor

