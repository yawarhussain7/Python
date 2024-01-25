print("TOpic: Set Method in Python ")

s1 = {1,2,3,4,5}
s2 = {1,4,7,2,8}
# Union 
union = s1.union(s2)
print(union)
# Intersection 
insection = s1.intersection(s2)
print(insection)
# Update 
s1.update(s2)
print(s1)
#Sematric Difference 
country1 = {"Pakistan","India","China","Iran","Afgunistan"}
country2 = {"Pakistan","Iran","Afgunistan"}

country3 = country1.symmetric_difference(country2)
print(country3)

#Subset 
sub_01 = country1.issubset(country2)
print(sub_01)
#Disjoin
sub_02 = country1.isdisjoint(country2)
print(sub_02)
#Super Set
counter = {"Pakistan","China"}
sub_03 = country1.issuperset(counter)
print(sub_03)
#add 
country1.add("Malishiya")
print(country1)
#remove
country1.remove("China")
print(country1)
#pop : remove random value
items = {2,3,5,7,81,212}
items.pop();
print(items)
#del 
city = {"lahore","karachi","abbottbad"}
del city
# print(city)   Give error because city does't exist
#clear
city_01 = {"AMalpura","Gulzar-e-QUail","ALipur","jinaabad"}
city_01.clear()
print(city_01)

if "Pakistan" in country1:
    print("Pakistan is Include ")
else:
    print("ERROR")
