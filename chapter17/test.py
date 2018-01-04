import requests


url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(r.json())
