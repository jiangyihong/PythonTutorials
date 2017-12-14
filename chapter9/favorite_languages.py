from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages["jen"] = "python"
favorite_languages["sarah"] = "c"
favorite_languages["edward"] = "ruby"
favorite_languages["phil"] = "python"

for name, language in favorite_languages.items():
    print("{0} 's favorite language is {1}".format(name.title(), language.title()))
