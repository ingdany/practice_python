class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Drive!")
        
class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Fly!")

car1 = Car("Toyota", "Corolla")
boat1 = Boat("Bavaria", "C45")
plane1 = Plane("Boeing", "737")

for x in (car1, boat1, plane1):
    x.move()
