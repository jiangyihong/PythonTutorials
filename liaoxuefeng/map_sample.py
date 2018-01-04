def f(x):
    return x * x


result = map(f, range(1, 10))
print(list(result))

str_list = list(map(str, range(1, 11)))
print(str_list)
