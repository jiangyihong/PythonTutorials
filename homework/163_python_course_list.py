import requests
from bs4 import  BeautifulSoup

url = "http://study.163.com/category/python#/?p=1"
web_data = requests.get(url)
soup = BeautifulSoup(web_data.text,"lxml")
print(soup)