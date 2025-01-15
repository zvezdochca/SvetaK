from smartphone import Smartphone


catalog = [
    Smartphone("Nokia", "1100", "+79032223322"),
    Smartphone("Apple", "iPhone 6", "+79033333333"),
    Smartphone("Motorola", "Razr V3", "+79035555555"),
    Smartphone("Samsung", "SGH-E250", "+79033338888"),
    Smartphone("Apple", "iPhone 10", "+79035699999")
]


for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. "
          f"{smartphone.subscriber_number}")
