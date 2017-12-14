class Restaurant(object):
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

    def read_number_served(self):
        print(self.number_served)


restaurant = Restaurant("全聚德", "烤鸭店")
restaurant.set_number_served(1000)
restaurant.read_number_served()
restaurant.increment_number_served(10)
restaurant.read_number_served()

