# Exercise 2: Static Method for Utility Calculation Instruction:

# Create a class Calculator with static methods for basic
# mathematical operations like addition and multiplication.
# Implement static methods add() and multiply() to perform these operations.


class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b


print(Calculator.add(2, 4))
print(Calculator.multiply(2, 4))
