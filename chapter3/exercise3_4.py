names = ['张三','李四','王五','赵六']
print(names)
unreach_person = names[1]
names[1] = '田七'
print(unreach_person)
names.insert(0,'曹操')
names.insert(2,'关羽')
names.append('张辽')
print(names)
names.pop()
names.pop()
names.pop()
names.pop()
names.pop()
print(names)
del names[0]
del names[0]
print(names)

