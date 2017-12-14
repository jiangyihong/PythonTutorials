filename = "guest_book.txt"

while True:
    name = input("Please input your name:")
    if name == "q":
        break
    else:
        with open(filename, "a", encoding="utf8") as file_object:
            file_object.write(name + "\n")