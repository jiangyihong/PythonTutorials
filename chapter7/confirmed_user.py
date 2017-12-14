unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# 验证每个用户直到用户中没有任何为验证的用户为止
# 将每个验证过的用户添加到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print('Verifying user: %s ' % current_user)
    confirmed_users.append(current_user)
print('\n The following users have been confirmed:')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
