def build_person(first_name, last_name, age=""):
    """返回一个字典，其中包含有一个人的信息"""
    person = {"first_name": first_name, "last_name": last_name}
    if age:
        person["age"] = age
    return person


musician = build_person("jimi", "hendrix", 27)
print(musician)
