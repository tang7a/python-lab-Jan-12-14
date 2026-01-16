class BankAccount:
    def __init__(self, balance):
        self._balance = balance   # private attribute (by convention)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount

    def get_balance(self):
        return self._balance


account = BankAccount(100)

account.deposit(50)
print(account.get_balance())

account.withdraw(30)
print(account.get_balance())

account.withdraw(200)
print(account.get_balance())