import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

URL = "https://api.github.com/search/repositories?q=language:C%23&sort=stars"
r = requests.get(url=URL)
response_dicts = r.json()

# 获取星级最多的相关仓库列表
repo_dicts = response_dicts["items"]

names, stars = [], []
for repo in repo_dicts:
    names.append(repo["name"])
    stars.append(repo["stargazers_count"])

# 数据可视化
my_style = LS("#333366", base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = "Most-Starred C# Projects on GitHub"
chart.x_labels = names

chart.add("", stars)
chart.render_to_file("csharp_repos.svg")
