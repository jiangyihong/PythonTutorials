import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("status_code:" + str(r.status_code))
response_dict = r.json()
print("Total repositories:", response_dict["total_count"])

# 研究有关仓库信息
repo_dicts = response_dict["items"]

names, plot_dicts = [], []
for repo in repo_dicts:
    names.append(repo["name"])
    plot_dict = {
        "value": repo["stargazers_count"],
        "label": str(repo["description"]),
        "xlink": str(repo["html_url"])
    }
    plot_dicts.append(plot_dict)
# 数据可视化
my_style = LS("#333366", base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(my_config, style=my_style)
chart.title = "Most-Starred Python Projects on GitHub"
chart.x_labels = names

chart.add("", plot_dicts)
chart.render_to_file("python_repos.svg")


