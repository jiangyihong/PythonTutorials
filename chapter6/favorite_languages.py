favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
# for name, language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " +
#           language.title() + '.')
# for value in favorite_languages.values():
#     print(value.title())
# for key in sorted(favorite_languages.keys()):
#     print(key)
# for language in favorite_languages.values():
#     print(language)
for language in set(favorite_languages.values()):
    print(language.title())

