class BankAccount:
    interest_rate = 0.02
    def __init__(self, owner_name, balance):
        self.__owner_name = owner_name
        self.__balance = balance

    @property
    def owner_name(self):
        return self.__owner_name

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Balance cannot be negative")
            return
        self.__balance = amount

    def deposit(self, amount):
        if amount <= 0:
            print(" Deposit amount must be positive")
            return False
        self.__balance += amount
        return True
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
            return False
        if amount > self.__balance:
            print("Insufficient funds")
            return False
        self.__balance -= amount
        return True
    def apply_interest(self):
        interest= self.__balance * self.interest_rate
        interest_amount = self.__balance + interest
        return interest_amount

    def display_info(self):
        print(f"Account Owner: {self.owner_name}")
        print(f"Balance: ${self.balance}")
        print(f"Interest Rate: {self.interest_rate * 100}%")

# run the code
account = BankAccount("Ally", 2000)

# perform operations
account.deposit(500)
account.withdraw(200)
account.apply_interest()

# display account information
account.display_info()

# test setter
account.balance = 500
print(f"Balance after setter: ${account.balance}")

# test withdrawal
account.withdraw(10000)
print(f"Final balance: ${account.balance}")