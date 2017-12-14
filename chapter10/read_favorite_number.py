import json


filename = "favorite_number.json"
with open(filename) as file_object:
    favorite_number = json.load(file_object)
    print("Your favorite number is {0}".format(favorite_number))
