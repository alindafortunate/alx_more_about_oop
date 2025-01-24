from phone import Phone

phone1 = Phone("Infinix Hot 8", 300, 6)
phone1.increment_price(0.5)
print(phone1.price)
phone1.send_email()
