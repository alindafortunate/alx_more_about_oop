class Item:
    pay_rate = 0.8  # Pay rate after 20% discount

    def __init__(self, name: str, price: float, quantity=0):
        # Run validation to the received arguments.
        assert price >= 0, f"Price:{price} can't be less or equal to zero."
        assert quantity >= 0, f"Quantity:{quantity} can't be less or equal to zero."

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = (
            self.price * self.pay_rate
        )  # Take note of how I acess a pay_rate attribute inside a method (Item.pay_rate).
        #  Though better to add self so that it is accessed from the instance level.


item1 = Item("Phone", 100, 3)

item2 = Item("Laptop", 2000, 4)

# print(item1.calculate_total_price())
# print(item2.calculate_total_price())
# print(item1.pay_rate)
# # Accessing all the attribute of the class and the object.
# print(Item.__dict__)  # Attributes for the class.
# print()
# print(item1.__dict__)  # All attributes for the instance/object.

item1.apply_discount()
print(item1.price)

item2.pay_rate = 0.9
item2.apply_discount()
print(item2.price)
