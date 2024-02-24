from bs4 import BeautifulSoup 
print("Topic: Request Module in Python ")


import requests

# respone = requests.get("https://www.facebook.com")

# print(respone.text)

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title":'Yawar Hussain',
    "body":'bar',
    "userid":122,
}
headers = {
    'Content-type':'application/json; charset = UTF-8',
}
respone = requests.post(url,headers=headers,json=data)
print(respone.text)


newurl = "https://www.codewithharry.com/blogpost/django-cheatsheet/"

r = requests.get(newurl)

print(r.text)


soup = BeautifulSoup(r.text,'html.parser')

print(soup.prettify())