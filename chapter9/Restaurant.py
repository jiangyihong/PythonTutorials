class Restaurant(object):
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("{0}\t{1}".format(self.restaurant_name, self.cuisine_type))

    def open_restaurant(self):
        print("Restaurant is opening!")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["apple", "orange", "strawberry"]

    def describe_flavors(self):
        print("We have {0},{1},{2} .etc flavored  ice cram".format(self.flavors[0], self.flavors[1], self.flavors[2]))


restaurant = Restaurant("全聚德", "烤鸭店")
restaurant.open_restaurant()
restaurant.describe_restaurant()
ice_cream_stand = IceCreamStand("哈根达斯", "冰激凌店")
ice_cream_stand.describe_flavors()
