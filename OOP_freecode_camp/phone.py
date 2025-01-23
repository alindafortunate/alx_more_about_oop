from item import Item


class Phone(Item):

    def __init__(self, name, price, broken_phones=0, quantity=0):
        super().__init__(name, price, quantity)
        self.broken_phones = broken_phones

    def phones_for_self(self):
        self.quantity -= self.broken_phones
        return f"Good phones:{self.quantity}"
