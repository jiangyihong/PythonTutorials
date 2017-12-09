import requests
import os
import time
from bs4 import BeautifulSoup


def get_all_page_url():
    page_url_list = []
    base_url = "http://www.mmjpg.com/"
    for page in range(1, 80):
        if page == 1:
            current_url = base_url
        else:
            current_url = base_url + "home/" + str(page)
        page_url_list.append(current_url)
    get_all_albums(page_url_list)


# 获取所有的相册列表
def get_all_albums(page_list):
    album_list = []
    for current_page_url in page_list:
        get_current_page_albums(current_page_url, album_list)
    for album in album_list:
        get_album_photos(album["url"])
        time.sleep(1)


# 获取当前页面的所有相册
def get_current_page_albums(page_url, album_list):
    web_data = requests.get(page_url)
    html = BeautifulSoup(web_data.text, "lxml")
    albums_li_list = html.select("li")
    # 遍历每个li标签获取当前相册的地址和标题
    for albums_li in albums_li_list:
        title = albums_li.select("a > img")[0].get("alt")
        url = albums_li.select("a")[0].get("href")
        album = {
            "title": title,
            "url": url
        }
        album_list.append(album)


# 获取所有相册中的所有图片
def get_album_photos(album_url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'CG-Sid': 'pWytfnWW-0Al4ZSlV-Bq4UCxrh-ArbOutkJ-h54hGTwV-A+Wg04d8-uELSEpB/-S9A61XA8',
        'CG-Ver': '1.6.5',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Host': 'www.mmjpg.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }
    web_data = requests.get(album_url, headers=headers)
    soup = BeautifulSoup(web_data.text, "lxml")
    title = soup.select("div.article > h2")[0].text
    page_count = int(soup.select("div.page > a")[-2].text)
    first_image_url = soup.select("#content > a > img")[0].get("src")
    base_image_url, image_name = os.path.split(first_image_url)
    for index in range(1, page_count + 1):
        picture_name = str(index) + ".jpg"
        picture_url = base_image_url + "/" + str(index) + ".jpg"
        download_image(title, picture_url, picture_name)
        # 主线程休眠3秒 防止并发过大 服务器连接超时
        time.sleep(3)


def download_image(title, image_url, image_name):
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


get_all_page_url()
