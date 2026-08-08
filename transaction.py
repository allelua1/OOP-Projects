# transaction class for recording financial activities
class Transaction:
    # Initialize transaction with transaction_type, amount, and account
    def __init__(self, transaction_type, amount, account):
        self.transaction_type = transaction_type
        self.amount = amount
        self.account = account

        # Return formatted string representation of the transaction
    def __str__(self):
        return f"{self.transaction_type.title()} - ${self.amount:.2f}"
# transaction  = Transaction("saving", 3000, "S123")    
# print(transaction)