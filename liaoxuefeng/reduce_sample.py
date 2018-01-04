from functools import reduce


def add(x, y):
    return x + y


sum_result = reduce(add, range(1, 11))
print(sum_result)
