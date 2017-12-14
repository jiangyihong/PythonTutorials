from chapter9.admin_user import Admin
import chapter9.user

user = chapter9.user.User("Jason", "Bourne", 29)
user.describe_user()
user.greet_user()
administrator = Admin("Jack", "Smith", 19)
administrator.privileges.show_privileges()
