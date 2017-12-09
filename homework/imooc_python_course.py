import requests
import json
from bs4 import  BeautifulSoup


url = "https://www.imooc.com/course/list?c=python"
web_data = requests.get(url)
soup = BeautifulSoup(web_data.text, "lxml")
course_item_list = soup.select("div.course-card-container")
course_list = []
for course_item in course_item_list:
    title_list = course_item.select("h3.course-card-name")
    title = title_list[0].text
    summary_list = course_item.select("p.course-card-desc")
    summary = summary_list[0].text
    level_list = course_item.select("div.course-card-info > span")
    level = level_list[0].text
    # view_count_list = course_item.select("")
    # view_count = view_count_list[0].text
    link_list = course_item.select("a.course-card")
    link = link_list[0].get("href")
    course = {
        "title": title,
        "summary": summary,
        "level": level,
        # "view_count": view_count,
        "link": "http://www.imooc" + link
    }

    course_list.append(course)
    json_data = json.dumps(course_list, ensure_ascii=False, indent=2)
    with open("course_list.txt", "w") as file_object:
        file_object.write(json_data)
    print(json_data)
