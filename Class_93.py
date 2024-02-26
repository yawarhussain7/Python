import requests
import json

query = input("What type of news you are intrested ")
url = "https://newsapi.org/v2/everything?q{query}=tesla&from=2024-01-26&sortBy=publishedAt&apiKey=0a0e1ad8c7e140dc81e8116cf818f986"

r = requests.get(url)

print(r.text)

news = json.loads(r.text)
# print(news,type(news))

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
