import requests
import time
from bs4 import BeautifulSoup


def get_time_info(link):
    web_data = requests.get(link)
    soup = BeautifulSoup(web_data.text, "lxml")
    # 抓取标题
    title_list = soup.select('h1.info_titile')
    title = title_list[0].text

    # 抓取价格
    price_list = soup.select('span.price_now > i')
    price = price_list[0].text

    # 抓取浏览量
    views_list = soup.select('span.look_time')
    views = views_list[0].text

    # 抓取城市
    area_list = soup.select('div.palce_li > span > i')
    area = area_list[0].text

    category_list = soup.select('span.crb_i > a')
    category = category_list[-1].text.strip()

    data = {
        "title": title,
        "views": views,
        "price": price,
        "area": area,
        "category": category
    }

    print(data)


def get_all_item_info(link):
    # url = "http://bj.58.com/pbdn/"
    web_data = requests.get(link)
    soup = BeautifulSoup(web_data.text, "lxml")
    href_list = soup.select("a.t")
    for href in href_list:
        link = href.get("href")
        if "zhuanzhuan" in link:
            get_time_info(link)
        time.sleep(3)


# count = 0
# while count < 100:
#     url = "http://bj.58.com/pbdn/pn"+str(count)+"/?PGTID=0d305a36-0000-1810-ae2f-f25a5d398fe0&ClickID=2"
#     count += 1
#     get_all_item_info(url)
print("中文")


