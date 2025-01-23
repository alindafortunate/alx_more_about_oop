import csv


class Item:
    pay_rate = 0.8  # Pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validation to the received arguments.
        assert price >= 0, f"Price:{price} can't be less or equal to zero."
        assert quantity >= 0, f"Quantity:{quantity} can't be less or equal to zero."

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        # Return them in a list format.
        Item.all.append(
            self
        )  # Not that self is the same as the instance that will be created.

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = (
            self.price * self.pay_rate
        )  # Take note of how I acess a pay_rate attribute inside a method (Item.pay_rate).
        #  Though better to add self so that it is accessed from the instance level.

    # Defining a class method
    @classmethod
    def instanciate_from_csv(cls):
        with open("items.csv", "r") as file:
            content = csv.DictReader(file)
            items = list(content)
        for item in items:
            Item(
                name=item["name"],
                price=float(item["price"]),
                quantity=int(item["quantity"]),
            )

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"


class Phone(Item):

    def __init__(self, name, price, broken_phones=0, quantity=0):
        super().__init__(name, price, quantity)
        self.broken_phones = broken_phones

    def phones_for_self(self):
        self.quantity -= self.broken_phones
        return f"Good phones:{self.quantity}"


# print(item1.calculate_total_price())
# print(item2.calculate_total_price())
# print(item1.pay_rate)
# # Accessing all the attribute of the class and the object.
# print(Item.__dict__)  # Attributes for the class.
# print()
# print(item1.__dict__)  # All attributes for the instance/object.

# item1.apply_discount()
# print(item1.price)

# item2.pay_rate = 0.9
# item2.apply_discount()
# print(item2.price)

# item1 = Item("Phone", 100, 3)
# item2 = Item("Laptop", 2000, 4)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)

#  Think of how best to return them in a list.
# print(Item.all)

# # Listing all the names of the instances.
# for instance in Item.all:
#     print(instance.name)
# Item.instanciate_from_csv()
# print(Item.all)
# print(Item.is_integer(5.5))

phone1 = Phone("Sumsang", 500, 2, 5)
print(phone1.phones_for_self())
print(phone1.calculate_total_price())
print(Item.all)
