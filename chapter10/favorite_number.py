import json


def get_stored_favorite_number():
    filename = "favorite_number.json"
    try:
        with open(filename) as file_object:
            favorite_number = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return favorite_number


def get_new_favorite_number():
    filename = "favorite_number.json"
    favorite_number = input("Please input your favorite number:")
    with open(filename, "w") as file_object:
        json.dump(favorite_number, file_object)
    return favorite_number


def show_favorite_number():
    favorite_number = get_stored_favorite_number()
    if favorite_number:
        print("I know your favorite number! It's {0}".format(favorite_number))
    else:
        favorite_number = get_new_favorite_number()
        print("Your favorite number is {0}".format(favorite_number))


show_favorite_number()
