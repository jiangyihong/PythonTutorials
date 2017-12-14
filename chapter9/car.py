class Car(object):
    def __init__(self, make, model, year):
        """初始化汽车的描述信息"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = "{0} {1} {2}".format(self.year, self.make, self.model)
        return long_name.title()

    def read_odometer(self):
        print("This car has {0} miles on it".format(self.odometer_reading))

    def update_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, mileage):
        self.odometer_reading += mileage
