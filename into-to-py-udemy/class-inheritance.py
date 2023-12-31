# OOP - class inheritance

class Car:
    def __init__(self):
        self.wheels = 4
        self.seats = 5
    
    def drive(self):
        print("Driving a car...")


class SportsCar(Car):
    def __init__(self):
        super().__init__()
        self.engine_power = '400 HP'
        self.seats = 2

    def drive(self):
        print("Driving a sports car...")


myCar = Car()
myCar.drive()

mySportsCar = SportsCar()
mySportsCar.drive()