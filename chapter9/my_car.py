from chapter9.car import Car
from chapter9.electric_car import ElectricCar

my_new_car = Car("audi", "a4", 2017)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()


my_tesla = ElectricCar("tesla", "model s", 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()


