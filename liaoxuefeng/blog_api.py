import requests


url = 'https://www.liaoxuefeng.com'
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'CG-Sid': 'pWytfnWW-0Al4ZSlV-Bq4UCxrh-ArbOutkJ-h54hGTwV-A+Wg04d8-uELSEpB/-S9A61XA8',
    'CG-Ver': '1.6.5',
    'Connection': 'keep-alive',
    'Content-Length': '24',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'user_trace_token=20171203202054-689b0582-d824-11e7-bec2-525400f775ce; LGUID=20171203202054-689b0a2c-d824-11e7-bec2-525400f775ce; JSESSIONID=ABAAABAACEBACDG77BB5661B87C6220073DD3C43039E516; _gat=1; PRE_UTM=; PRE_HOST=www.google.com; PRE_SITE=https%3A%2F%2Fwww.google.com%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; index_location_city=%E5%85%A8%E5%9B%BD; SEARCH_ID=dcf50f3698c9424282ea8b7d632c03d5; _gid=GA1.2.2015093765.1512484136; _ga=GA1.2.201802496.1512303655; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1512303664,1512484136,1512490628; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1512490642; LGSID=20171206001711-bff491a6-d9d7-11e7-8571-525400f775ce; LGRID=20171206001725-c82ba443-d9d7-11e7-8571-525400f775ce; TG-TRACK-CODE=search_code',
    'DNT': '1',
    'Host': 'www.liaoxuefeng.com',
    'Origin': 'https://www.liaoxuefeng.com',
    'Referer': 'https://www.liaoxuefeng.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'X-Anit-Forge-Code': '0',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With': 'XMLHttpRequest'
}
data = requests.get(url)
print(data)

