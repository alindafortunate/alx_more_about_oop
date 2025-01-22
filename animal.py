class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Generic animal sound.")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        print("Woof!")


dog = Dog("German Shepherd", "Labrador")
dog.make_sound()
