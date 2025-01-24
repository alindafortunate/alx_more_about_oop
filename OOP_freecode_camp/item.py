import csv


class Item:
    pay_rate = 0.8  # Pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        # Run validation to the received arguments.
        assert price >= 0, f"Price:{price} can't be less or equal to zero."
        assert quantity >= 0, f"Quantity:{quantity} can't be less or equal to zero."

        # Assign to self object
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Return them in a list format.
        Item.all.append(
            self
        )  # Not that self is the same as the instance that will be created.

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value

    def increment_price(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    @property  # Property decorator for read only.
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("Your name is more than 10 characters.")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.__price * self.quantity

    def apply_discount(self):
        self.__price = (
            self.__price * self.pay_rate
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

    def __connect_to_smtp_server(self, smtp_server):
        pass

    def __prepare_message_body(self):
        return f"""
                Hello John.............
                """

    def __send(self):
        pass

    def send_email(self):
        self.__connect_to_smtp_server(smtp_server="aas")
        self.__prepare_message_body()
        self.__send()

    def __repr__(self):
        return (
            f"{self.__class__.__name__}('{self.__name}',{self.__price},{self.quantity})"
        )
