class Product:
    def __init__(self, name, price, quantity):
        self._name = name
        self._price = price if price >= 0 else 0
        self._quantity = quantity

    def sell(self, amount):
        if amount <= 0 or amount > self._quantity:
            return False
        self._quantity -= amount
        return True

    def restock(self, amount):
        if amount <= 0:
            return False
        self._quantity += amount
        return True

    def get_product_info(self):
        return self._name, self._price, self._quantity


p = Product("Notebook", 5.00, 10)
print(p.get_product_info())
p.sell(3)
p.restock(5)
print(p.get_product_info())