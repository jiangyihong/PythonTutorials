# coding:utf-8
import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    url = 'http://news.qq.com/'
    # 请求腾讯新闻获取html
    web_data = requests.get(url).text
    # 对html进行格式化
    html = BeautifulSoup(web_data, "lxml")
    # 筛选出新闻节点
    news_list = html.select('div.text > em.f14 > a.linkto')
    for news in news_list:
        title = news.get_text()
        link = news.get('href')
        data = {
            '标题': title,
            '链接': link
        }
        print(data)
