def count():
    def g(j):
        def fun():
            return j * j
        return fun

    function_list = []
    for i in range(1, 4):
        function_list.append(g(i))
    return function_list


function1, function2, function3 = count()

print(function1())
print(function2())
print(function3())
