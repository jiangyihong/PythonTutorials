import requests
import json
import pymongo


url = 'http://www.toutiao.com/api/pc/focus/'
web_data = requests.get(url)


json_data = json.loads(web_data.text)
news_list = json_data['data']['pc_feed_focus']

conn = pymongo.MongoClient(host='localhost', port=27017)
focus_collection = conn['focus']
news_data = focus_collection['news']

for news in news_list:
    news_data.insert_one(news)
news_data.find()
conn.close()
conn.close_cursor()
