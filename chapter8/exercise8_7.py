def make_album(singer, album_name, count=""):
    album = { "singer_name": singer, "album": album_name}
    if count:
        album["count"] = count
    return album


print(make_album("刘若英", "为爱痴狂", 8))
print(make_album("梁静茹", "勇气"))
print(make_album("卓依婷", "燃烧", 10))

