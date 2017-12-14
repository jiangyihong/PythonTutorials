filename = "programming.txt"

# with open(filename, "w", encoding="utf8") as file_object:
#     file_object.write("I love programming!\n")
#     file_object.write("人生苦短，我用python!\n")
with open(filename, "a", encoding="utf8") as file_object:
    file_object.write("I also love finding meaningin large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
