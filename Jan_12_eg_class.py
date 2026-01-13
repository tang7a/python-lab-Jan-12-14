class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def apply_discount(self, percent):
        self.price *= (1 - percent / 100)

    def restock(self, amount):
        self.quantity += amount


# Testing
p1 = Product("Notebook", 5.00, 20)
p2 = Product("Pen", 2.00, 100)

print(p1.name, p1.total_value())
print(p2.name, p2.total_value())

p1.apply_discount(10)
p2.restock(50)

print(p1.name, p1.price, p1.quantity, p1.total_value())
print(p2.name, p2.price, p2.quantity, p2.total_value())