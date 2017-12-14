import json


def get_stored_username():
    """如果存储了用户名，就获取它"""
    filename = "username.json"
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """获取用户名，并存储到文件中"""
    username = input("What is your name?")
    filename = "username.json"
    with open(filename, "w") as file_object:
        json.dump(username, file_object)
    return username


def greet_user():
    """问候用户，并指出名字"""
    # 获取存储的用户名
    username = get_stored_username()
    if username:
        # 询问用户用户名是否一致
        flag = input("Is '{0}' your username?".format(username))
        if flag == "y":
            print("Welcome back, {0}".format(username))
        else:
            new_username = get_new_username()
            print("We'll remember you when come back, {0}".format(new_username))
    else:
        new_username = get_new_username()
        print("We'll remember you when come back, {0}".format(new_username))


greet_user()
