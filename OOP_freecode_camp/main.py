from item import Item


item1 = Item("MyItem", 1000)
item1.name = "OtherItem"
print(item1.name)
# item1.price = 12000
# print(item1.price)
item1.increment_price(0.5)
print(item1.price)
