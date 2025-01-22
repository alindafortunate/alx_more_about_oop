class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}"


class CLothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def __str__(self):
        return f"{self.name}, {self.price}, {self.size}"


men = CLothing("Shirt", 20, "M")
print(men)
