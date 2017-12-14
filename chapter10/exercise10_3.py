name = input("Please input your name:")
filename = "visitors.txt"
with open(filename, "w", encoding="utf8") as file_object:
    file_object.write(name)
