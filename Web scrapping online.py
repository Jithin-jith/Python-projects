from bs4 import BeautifulSoup
import requests

url = "https://www.geeksforgeeks.org/introduction-deep-learning/"
result = requests.get(url)

doc = BeautifulSoup(result.text,'html.parser')

#print(doc.prettify())

title  = doc.find_all('div',{"class": "article-title"})[0].text
print(type(title))
print(title)