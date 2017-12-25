from bs4 import BeautifulSoup
import requests


def generate_page_url():
    url_format = "https://movie.douban.com/top250?start={0}&filter="
    url_list = [url_format.format(index * 25) for index in range(0, 10)]
    print(url_list)

