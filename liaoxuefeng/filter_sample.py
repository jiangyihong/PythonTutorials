def is_odd(number):
    return number % 2 == 1


odd_list = list(filter(is_odd, range(1, 11)))
print(odd_list)
