import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
import pymysql


def get_job(page):
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%85%A8%E5%9B%BD&kw=python&kt=3&sg=c31dcc725fe64a309ebbc5535b63904d&p={0}'.format(
        page)
    print("第{0}页".format(page))
    headers = {
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'accept-encoding': "gzip, deflate",
        'accept-language': "zh-CN,zh;q=0.9,en;q=0.8",
        'cache-control': "no-cache",
        'connection': "keep-alive",
        'cookie': "adfbid=0; adfbid2=0; dywea=95841923.2541085876582646000.1515073512.1515073512.1515073512.1; dywec=95841923; dywez=95841923.1515073512.1.1.dywecsr=google.com|dyweccn=(referral)|dywecmd=referral|dywectr=undefined|dywecct=/; __utma=269921210.441085162.1515073512.1515073512.1515073512.1; __utmc=269921210; __utmz=269921210.1515073512.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); Hm_lvt_38ba284938d5eddca645bb5e02a02006=1515073512; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1515073512; JSSearchModel=0; LastCity%5Fid=489; LastCity=%e5%85%a8%e5%9b%bd; BLACKSTRIP=yes; urlfrom=121126445; urlfrom2=121126445; adfcid=none; adfcid2=none; __utmt=1; LastSearchHistory=%7b%22Id%22%3a%224c2dfdb7-a445-47db-96c2-abd09de83959%22%2c%22Name%22%3a%22python+%2b+%e5%85%a8%e5%9b%bd%22%2c%22SearchUrl%22%3a%22http%3a%2f%2fsou.zhaopin.com%2fjobs%2fsearchresult.ashx%3fjl%3d%25e5%2585%25a8%25e5%259b%25bd%26kw%3dpython%26kt%3d3%26sg%3dc31dcc725fe64a309ebbc5535b63904d%26p%3d3%22%2c%22SaveTime%22%3a%22%5c%2fDate(1515074370660%2b0800)%5c%2f%22%7d; dyweb=95841923.21.6.1515073575214; __utmb=269921210.21.9.1515073575215",
        'dnt': "1",
        'host': "sou.zhaopin.com",
        'referer': "http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%e5%85%a8%e5%9b%bd&kw=python&kt=3&sg=c31dcc725fe64a309ebbc5535b63904d&p=2",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
        'postman-token': "773af6fa-a0a2-4719-c7cd-bf5a59acc607"
    }
    web_data = requests.get(url, headers=headers).text
    html = BeautifulSoup(web_data, 'lxml')
    job_list = html.select('table.newlist > tr > td.zwmc > div > a')
    company_name_list = html.select('table.newlist > tr > td.gsmc > a')
    salary_list = html.select('table.newlist > tr > td.zwyx')
    location_list = html.select('table.newlist > tr > td.gzdd')
    for job_name, company, salary, location in zip(job_list, company_name_list, salary_list, location_list):
        data = {
            'job_name': job_name.get_text(),
            'company': company.get_text(),
            'salary': salary.get_text(),
            'location': location.get_text()
        }
        print(data)


if __name__ == '__main__':
    pool = Pool()
    for page in range(1, 387):
        pool.apply_async(get_job, args=(page,))
    print('启动进程')
    pool.close()
    pool.join()
