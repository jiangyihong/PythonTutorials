# while True:
#     prompt = '请输入观众的年龄:'
#     age_str = input(prompt)
#     age = int(age_str)
#     if age < 3:
#         print('免费')
#     elif 3 <= age <= 12:
#         print('10￥')
#     else:
#         print('15￥')


# prompt = '请输入观众的年龄:'
# message = ''
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         age = int(message)
#         if age < 3:
#             print('免费')
#         elif 3 <= age <= 12:
#             print('10$')
#         else:
#             print('15$')
#     else:
#         print('bye')

# prompt = '请输入观众的年龄：'
# active = True
# while active:
#     message = input(prompt)
#     if message != 'quit':
#         age = int(message)
#         if age < 3:
#             print('免费')
#         elif 3 <= age <= 12:
#             print('10￥')
#         else:
#             print('15￥')
#     else:
#         active = False
#         print('bye')


prompt = '请输入观众的年龄：'
while True:
    message = input(prompt)
    if message == 'quit':
        print('bye')
        break
    else:
        age = int(message)
        if age < 3:
            print('免费')
        elif 3 <= age <= 12:
            print('10￥')
        else:
            print('15￥')


