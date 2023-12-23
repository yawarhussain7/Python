print("THis is Data type and variable in Python programming language ")

number = 3
decimal = 6.4
complexnumber = complex(4,2)
string = "Yawar Hussain"
char = 'c'

list = [
    [234,45,23],
    ["Yawar","HUssain"],        # List is mutable data type
    [12.4,43.5],                # mutable mean we can change the value 

]

tuple = (
    ('Yawar ','Hussain'),
    (12,32,43),                 # tuple is Im mutable data type 
    (43.55,2.34),               # Im-Multabe mean we cannot change it value 

)

disct = {
    'Name':"Yawar",
    'No' : 122,
    'Uni':'COMSATS',
    'Section':'2D'
}


print("Number = ",number,type(number))
print("Decimal Number = ",decimal,type(decimal))
print("COmplex Number = ",complexnumber,type(complexnumber))
print("String = ",string,type(string))
print("Character = ",char,type(char))   # it is also string 
print("List = ",list,type(list))
print("Tuple = ",tuple,type(tuple))
print("DIct = ",disct,type(disct))
