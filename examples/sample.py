def calculate_total(items):
    total = 0
    for item in items:
        if item["price"] > 0:
            total += item["price"]
    return total

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
