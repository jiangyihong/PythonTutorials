# def get_formatted_name(first_name, last_name):
#     """返回整洁的姓名"""
#     full_name = first_name + " " + last_name
#     return full_name.title()


# def get_formatted_name(first_name, middle_name, last_name):
#     """返回整洁的姓名"""
#     full_name = first_name + ' ' + middle_name + ' ' + last_name
#     return full_name.title()


def get_formatted_name(first_name, last_name, middle_name=""):
    if middle_name:
        return first_name + " " + middle_name + " " + last_name
    else:
        return first_name + " " + last_name


musician = get_formatted_name("jimi", "hendrix")
print(musician)
