users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'aeinstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'mcurie',
        'location': 'paris',
    }
}

for username in users.keys():
    print('\nUserName: %s' % username)
    full_name = users[username]['first'] + ' ' + users[username]['last']
    location = users[username]['location']
    print('\tFull Name: %s' % full_name.title())
    print('\tLocation: %s' % location.title())
