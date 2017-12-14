import os
import requests
from bs4 import BeautifulSoup


def get_all_items(website):
    web_data = requests.get(website)
    html = BeautifulSoup(web_data.text, "lxml")
    item_list_html = html.select("div.card-box")
    picture_item_list = []
    for item_html in item_list_html:
        title_html = item_html.select("a.title-content")
        title = title_html[0].text
        url_html = item_html.select("a.title-content")
        picture_url = url_html[0].get("href")
        picture = {
            "title": title,
            "url": picture_url
        }
        if "work" in picture["url"]:
            picture_item_list.append(picture)
    return picture_item_list


def get_item_detail(picture_url, title):
    # 创建以标题命名的文件夹
    if not os.path.exists(title):
        os.mkdir(title)
    directory = os.getcwd() + "\\" + title
    web_data = requests.get(picture_url)
    html = BeautifulSoup(web_data.text, "lxml")
    image_list_html = html.select("div.reveal-work-wrap > img")
    for image_html in image_list_html:
        image_link = image_html.get("src").replace("128w", "1280w")
        print(image_link)
        download_image(image_link, directory)


def download_image(link, directory):
    file_directory, file_name = os.path.split(link)
    file_stream = requests.get(link)
    full_file_path = directory + "\\" + file_name
    with open(full_file_path, "wb") as file_object:
        file_object.write(file_stream.content)
    print(full_file_path)


url = "http://www.zcool.com.cn/discover/1!0!0!0!0!!!!2!-1!1"
print(url)
item_list = get_all_items(url)
for item in item_list:
    if "红头发女孩" in item["title"]:
        continue
    get_item_detail(item["url"], item["title"])
