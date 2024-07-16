class BankAccount:
    def __init__(self, initial_balance=0):
        self._account_balance = initial_balance

    def deposit(self, amount):
        self._account_balance += amount

    def withdraw(self, amount):
        if self._account_balance >= amount:
            self._account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        print("Current Balance: ${:.2f}".format(self._account_balance))