import functools


# def log(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kw):
#         print("begin call:")
#         result = func(*args, **kw)
#         print("after call")
#         return result
#
#     return wrapper

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("%s %s before call" % (text, func.__name__))
            result = func(*args, **kw)
            print("%s %s after call" % (text, func.__name__))
            return result

        return wrapper

    return decorator


@log("python ")
def say_hello():
    print("Hello World")


say_hello()
