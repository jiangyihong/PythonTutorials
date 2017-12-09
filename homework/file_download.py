import requests


url = "http://img.mmjpg.com/2017/919/2.jpg"

headers = {
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
'Cache-Control':'no-cache',
'Host':'img.mmjpg.com',
'Pragma':'no-cache',
'Proxy-Connection':'keep-alive',
'Referer':'http://www.mmjpg.com/mm/1185',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
}
web_data = requests.get(url, headers=headers)
with open("2.jpg", "wb") as file_object:
    file_object.write(web_data.content)
print("下载完成")
