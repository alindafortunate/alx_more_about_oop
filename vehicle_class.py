class Vehicle:
    def __init__(self, max_speed, color):
        self.max_speed = max_speed
        self.color = color

    def accelerate(self):
        print(f"The vehicle is accelarating with a speed of {self.max_speed}")


class Car(Vehicle):
    def __init__(self, max_speed, color):
        super().__init__(max_speed, color)
        self.max_speed = max_speed

    def accelerate(self):
        print(f"The car is accelerating with the speed of {self.max_speed}")


car1 = Car(100, "red")
car1.accelerate()

vehicle = Vehicle(250, "Blue")
vehicle.accelerate()
