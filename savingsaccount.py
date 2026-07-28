from account import Account
from transaction import Transaction

class SavingAccount(Account):
    def __init__(self, account_number, owner_name, balance=0, interest_rate=0.1, min_balance = 100):
        # TODO: Call parent constructor with account_number, owner_name, and balance
        super().__init__(account_number, owner_name, balance)
        # TODO: Store interest_rate as self.interest_rate (default 0.01)
        self.interest_rate = interest_rate
        # TODO: Store min_balance as self.min_balance (default 100)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if amount <= 0:
            return False, "Withdrawal amount must be positive"
        if amount > self.min_balance:
            return False, f"Cannot withdraw below minimum balance of ${self.min_balance:.2f}"
        self.min_balance -= amount
        transaction1 = Transaction("Withdrawal", amount, self)
        self.transaction_history.append(transaction1)
        return True, f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        transaction1 = Transaction("Interest", interest, self)
        self.transaction_history.append(transaction1)
        return True, f"Applied interest: ${interest:.2f}. New balance: ${self.balance:.2f}"