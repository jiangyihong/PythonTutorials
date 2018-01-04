from functools import reduce


def fn(x, y):
    return x * 10 + y


def char2int(c):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[c]


def str2int(s):
    number = reduce(fn, map(char2int, s))
    return number


def str2float(s):
    # 判断小数点的位数
    dot_index = s.rfind('.')
    # 获取当前浮点数字的整数形式
    s = s.replace('.', '')
    number = str2int(s)
    # 缩小相应的倍数 倍数是小数点的位数
    number = number / 10 ** dot_index
    return number


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
