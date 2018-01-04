import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("call %s():" % func.__name__)
        return func(*args, **kw)

    return wrapper


def log_text(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print("%s %s():" % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log_text("execute")
def now():
    print('2017-12-31')


now()
print(now.__name__)
