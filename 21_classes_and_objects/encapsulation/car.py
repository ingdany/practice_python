class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand


my_car = Car("Toyota", "Corolla")
print(my_car.get_brand())
my_car.set_brand("Ford")
print(my_car.get_brand())
# my_car = Car("Toyota", "Corolla")
# print(my_car.__brand)
