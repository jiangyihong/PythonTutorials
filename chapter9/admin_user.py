from chapter9.user import User


class Admin(User):

    def __init__(self, first_name: str, last_name: str, age: int) -> object:
        super(Admin, self).__init__(first_name, last_name, age)
        self.privileges = Privileges()


class Privileges(object):
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user", "can delete post", "can add user"]

    def show_privileges(self):
        print(self.privileges)
