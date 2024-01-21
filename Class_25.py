

print("<<==== Convert tupe into list =====>>\n")
countries = ("Span","Germany","Pakistan","India","Netherland")

print(type(countries))
print(countries)

temp = list(countries)
print(type(temp))
temp.append("Russia")

countries = tuple(temp)

print(countries)
print(type(countries))

print("<<==== Create New tuple =====>>\n")

country = ("Afganistan","Turkey","Iran","China")

newcountry = country + countries

print("New Country\n ",newcountry)


print("<<==== Count =====>>\n")

newtep = (3,54,7,8,3,2,67,2,1,67,8,4,3,2,1,6,3)
print(newtep.count(3))

print("<<==== Index =====>>\n")
print(newtep.index(2))

# newtep.index(number,starting_index,ending index )
inde = newtep.index(67,4,10)
print(inde)