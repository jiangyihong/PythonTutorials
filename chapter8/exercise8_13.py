def build_profile(first, last, **user_info):
    information = {"first_name": first, "last_name": last}
    for key, value in user_info.items():
        information[key] = value
    return information


user_profile = build_profile("Jason", "Bourne", birth="1970.9.13", contry="USA")
print(user_profile)
