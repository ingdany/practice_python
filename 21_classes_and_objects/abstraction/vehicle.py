from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Car(Vehicle):
    def start(self):
        print("The car is starting.")

    def move(self):
        print("The car is moving.")


class Boat(Vehicle):
    def start(self):
        print("The boat is sailing.")

    def move(self):
        print("The boat is moving.")


my_car = Car()
my_car.start()
my_car.move()
my_boat = Boat()
my_boat.start()
my_boat.move()
