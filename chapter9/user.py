class User(object):
    """模拟一个用户"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print("{0}\t{1}\t{2}".format(self.first_name, self.last_name, self.age))

    def greet_user(self):
        print("Hello, {0}.{1}".format(self.first_name.title(), self.last_name.title()))






