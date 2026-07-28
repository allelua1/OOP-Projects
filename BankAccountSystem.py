# Class BankAccount with attributes: owner, balance
# Methods: deposit, withdraw, check balance
# Subclasses: SavingsAccount (adds interest) and CurrentAccount (adds overdraft limit)
# Practices: inheritance, encapsulation

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposits(self, amount):
        self.balance += amount
        print(f"{amount} has been deposited successfully. ")
    def withdraw(self, amount):
        if self.balance < amount:
            print(" Insuficient balance. ")
        else:
            self.balance -= amount
            print(f"{amount} has been withdrawn successfull. ")
    def checkBalance(self):
        return self.balance


bank1 = BankAccount("Benigne", 20000)
print("Check Balance: ", bank1.checkBalance())

bank1.deposits(30000)
bank1.withdraw(8000)