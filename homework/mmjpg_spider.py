import requests
import os
from bs4 import BeautifulSoup


def download_image(title, image_url,image_name):
    headers = {
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'no-cache',
        'Host': 'img.mmjpg.com',
        'Pragma': 'no-cache',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://www.mmjpg.com/mm/1185',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }
    if not os.path.exists(title):
        os.mkdir(title)
    image_path = os.getcwd() + "\\" + title + "\\" + image_name
    web_data = requests.get(image_url, headers=headers)
    with open(image_path, "wb") as file_object:
        file_object.write(web_data.content)
    print(image_url)


url = "http://www.mmjpg.com/mm/919"
web_data = requests.get(url)
soup = BeautifulSoup(web_data.text, "lxml")
title = soup.select("div.article > h2")[0].text
page_count = int(soup.select("div.page > a")[-2].text)
first_image_url = soup.select("#content > a > img")[0].get("src")
base_image_url, image_name = os.path.split(first_image_url)
for index in range(1, page_count+1):
    picture_name = str(index) + ".jpg"
    picture_url = base_image_url + "/" + str(index) + ".jpg"
    download_image(title, picture_url, picture_name)
