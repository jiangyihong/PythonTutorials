def make_album(singer, singer_album_name):
    album_info = {"singer": singer, "album_name": singer_album_name}
    return album_info


while True:
    print("\nPlease tell me your favorite singer and album:")
    print("(enter 'q' at any time to exit)")
    singer_name = input("Singer:")
    if singer_name == "q":
        break
    album_name = input("Album:")
    if album_name == "q":
        break
    album = make_album(singer_name, album_name)
    print(album)

