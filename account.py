from abc import ABC, abstractmethod
from transaction import Transaction

class Account(ABC):
    def __init__(self, account_number, owner_name, balance = 0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount <= 0:
            return False, "Deposit amount must be positive"
        self.balance += amount
        transaction1 = Transaction("Deposit", amount, self)
        self.transaction_history.append(transaction1)
        return True, f"Deposited ${amount:.2f}. New Balance: ${self.balance:.2f}"

    def withdraw(self, amount):
        if amount <= 0:
            return False, "Withdrawal amount must be positive"
        if amount > self.balance:
            return False, "Insufficient funds"
        self.balance -= amount
        transaction1 = Transaction("Withdrawal", amount, self)
        self.transaction_history.append(transaction1)
        return True, f"Withdrew ${amount:.2f}. New Balance: ${self.balance:.2f}"
    def get_balance(self):
        return f"The current balance: $ {self.balance:.2f}"

    def get_transaction_history(self):
        return self.transaction_history
account = Account(123, "Allelua", 300)
print(account.deposit(200))
for t in account.get_transaction_history():
    print(t)

