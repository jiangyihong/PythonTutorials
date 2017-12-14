import json


filename = "username.json"
with open(filename) as file_object:
    username = json.load(file_object)
    print("Welcome back, {0}".format(username))

