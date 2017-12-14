# coding: utf-8
import requests
import json
import pymysql


url = 'http://www.toutiao.com/api/pc/focus/'
web_data = requests.get(url)


json_data = json.loads(web_data.text)
news_list = json_data['data']['pc_feed_focus']

conn = pymysql.connect(host='localhost', port=3306, user='root',
                       password='zxcv/8520', db='focus', charset='utf8')
cursor = conn.cursor()

for news in news_list:
    title = news['title']
    image_url = news['image_url']
    url = news['media_url']
    print(url, title, image_url)
    sql = "INSERT INTO news(Title,Url,ImageUrl) VALUES('{0}','{1}','{2}');"
    cursor.execute(sql.format(title, url, image_url))
    conn.commit()


cursor.close()
conn.close()
