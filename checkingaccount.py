from account import Account
from transaction import Transaction

class CheckingAccount(Account):
    def __init__(self, account_number, owner_name, balance=0, overdraft_limit = 100):
        super().__init__(account_number, owner_name, balance )
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        # TODO: Validate that amount is positive (> 0)
        # TODO: If invalid, return (False, "Withdrawal amount must be positive")
        if amount <= 0:
            return False, "Withdrawal amount must be positive"
        # TODO: Check if withdrawal would exceed overdraft limit
        if amount > self.overdraft_limit:
            # TODO: If exceeds limit, return (False, f"Cannot exceed overdraft limit of ${self.overdraft_limit:.2f}")
            return False, f"Cannot exceed overdraft limit of ${self.overdraft_limit:.2f}"
        # TODO: Subtract amount from self.balance
        self.balance -= amount
        # TODO: Create Transaction object with "withdrawal", amount, and self
        transaction1 = Transaction("Withdrawal", amount, self)
        # TODO: Append transaction to self.transaction_history
        self.transaction_history.append(transaction1)
        # TODO: If balance is negative, return message with "(Overdraft)" suffix
        if self.balance < 0:
            return "Overdraft"
        # TODO: Otherwise return normal withdrawal message
        # TODO: Format: (True, f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")
        return  True, f"Withdrew ${amount:.2f}. New Balance: ${self.balance:2f} "
