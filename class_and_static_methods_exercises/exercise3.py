# Exercise 3: Class Method for Factory Creation Instruction:

# Create a class Person with attributes name and age.
# Implement a class method create_child() to create a new instance representing a child with age set to 0.


class Person:
    all = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.all.append(self)

    @classmethod
    def create_child(cls, name, age=0):

        child = Person(name=name, age=age)

        for person in Person.all:
            print(person)

    def __repr__(self):
        return f"Name:{self.name}, Age:{self.age}"


Person.create_child("Alinda")

