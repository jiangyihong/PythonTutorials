from chapter9.car import Car


class ElectricCar(Car):
    def __init__(self, make: object, model: object, year: object) -> object:
        super().__init__(make, model, year)
        self.battery = Battery()


class Battery(object):
    """一次模拟电动汽车电瓶的简单尝试"""

    def __init__(self, battery_size: object = 70) -> object:
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a {0} -kWh battery".format(str(self.battery_size)))