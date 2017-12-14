peoples = {
    '张三':{
        'age':18,
        'city':'北京'
    },
    '李四':{
        'age':20,
        'city':'苏州'
    },
    '王五':{
        'age':26,
        'city':'上海'
    }
}

peoples['赵六'] = {
    'age':19,
    'city':'成都'
}

# for username,user_info in peoples.items():
#     print('\n %s ' % username)
#     age = user_info['age']
#     city = user_info['city']
#     print('\t %s ' % age)
#     print('\t %s ' % city)
for username in sorted(peoples.keys()):
    print(username)

