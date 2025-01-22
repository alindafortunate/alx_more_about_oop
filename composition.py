class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        self.engine.start()


class Engine:
    def __init__(self):
        pass

    def start(self):
        print("Engine starting......")


car = Car(Engine())
car.start()
