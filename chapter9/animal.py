class Animal(object):
    def __init__(self):
        pass

    def bark(self):
        print("Animal is barking!")


class Dog(Animal):
    def __init__(self):
        super().__init__()

    def bark(self):
        print("Dog is barking!")


class Cat(Animal):
    def __init__(self):
        super().__init__()

    def bark(self):
        print("Cat is barking!")


animal = Animal()
animal.bark()

my_dog = Dog()
my_dog.bark()

my_cat = Cat()
my_cat.bark()

