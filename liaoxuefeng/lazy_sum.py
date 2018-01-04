def lazy_sum(*args):
    def calc_sum():
        result = 0
        for n in args:
            result = n + result
        return result

    return calc_sum


sum_func = lazy_sum(1, 3, 5, 7, 9)
print(sum_func())
