import requests
from operator import itemgetter

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
headers = {
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'accept-encoding': "gzip, deflate, br",
    'accept-language': "zh-CN,zh;q=0.9,en;q=0.8",
    'cache-control': "no-cache",
    'connection': "keep-alive",
    'dnt': "1",
    'host': "hacker-news.firebaseio.com",
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
    'postman-token': "2b83a29d-5d6b-1eb9-ac04-61756b82bbdf"
}
r = requests.get(url, headers=headers)
print("Status code:", r.status_code)

submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # 对于每篇文章，都执行一个API调用
    submission_url = 'https://hacker-news.firebaseio.com/v0/item/{0}.json?print=pretty'.format(str(submission_id))
    submission_r = requests.get(submission_url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        'title': response_dict["title"],
        'link': 'https://nes.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0)
    }
    submission_dicts.append(submission_dict)
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)
for submission in submission_dicts:
    print("\nTitle:", submission["title"])
    print("Dicussion link", submission["link"])
    print("Comments", submission["comments"])
