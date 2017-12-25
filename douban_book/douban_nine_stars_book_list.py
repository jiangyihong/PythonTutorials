import requests
from bs4 import BeautifulSoup

url = 'https://www.douban.com/doulist/1264675/?start=150&sort=seq&sub_type='
web_data = requests.get(url)
with open('result.html', 'w', encoding='utf8') as file_object:
    file_object.write(web_data.text)
