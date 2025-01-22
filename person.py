class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def __str__(self):
        return f"Name:{self.name}, Age:{self.age}"


person = Person("Alinda", 27)
print(person)
