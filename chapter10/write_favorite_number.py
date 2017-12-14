import json

favorite_number_str = input("Please input your favorite number:")
filename = "favorite_number.json"
with open(filename, "w") as file_object:
    json.dump(favorite_number_str, file_object)
print("We'll remember your favorite number!")
