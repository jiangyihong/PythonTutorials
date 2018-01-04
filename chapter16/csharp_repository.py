import requests
import pygal

URL = 'https://api.github.com/search/repositories?q=language:C%23&sort=stars'
r = requests.get(url=URL)
response_dict = r.json()
repository_dict = response_dict["items"]

names, stars = [], []
for repository in repository_dict:
    names.append(repository["name"])
    stars.append(repository["stargazers_count"])

chart = pygal.Bar()
my_config = pygal.config.Config()
my_config.x_label_rotation = 45
chart.config = my_config
chart.title = "Most starred C# Project On GitHub"
chart.x_labels = names
chart.add("", stars)
chart.render_to_file("csharp_repository.svg")



