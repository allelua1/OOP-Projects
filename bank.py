from savingsaccount import SavingAccount
from checkingaccount import CheckingAccount

class Bank:
    def __init__(self, name):
        # TODO: Initialize bank with name
        # TODO: Store name as self.name
        self.name = name
        # TODO: Initialize empty dictionary for accounts as self.accounts
        self.accounts = dict()
    def create_account(self, account_type, account_number, owner_name, initial_balance = 0, **kwargs):
        # TODO: Check if account_number already exists in self.accounts
        # TODO: If exists, return (False, "Account number already exists")
        if account_number in self.accounts:
            return False, "Account number already exists"
        # TODO: Check account_type (case-insensitive)
        account_type = account_type.lower()
        # TODO: If "savings", create SavingsAccount with parameters and **kwargs
        if account_type == "savings":
            account = SavingAccount(account_number, owner_name, balance = initial_balance, **kwargs)
        # TODO: If "checking", create CheckingAccount with parameters and **kwargs
        elif account_type == "checking":
            account = CheckingAccount(account_number, owner_name, balance= initial_balance, overdraft_limit=100, *kwargs)
        # TODO: If invalid type, return (False, "Invalid account type")
        else :
            return False, "Invalid account type"
        # TODO: Store account in self.accounts with account_number as key
        self.accounts[account_number]= account
        # TODO: Return (True, f"{account_type.title()} account created successfully")
        return True, f"{account_type.title()} account created successfully"
    def get_account(self, account_number):
        # TODO: Return account from self.accounts dictionary using account_number as key
        return self.accounts.get(account_number)

        # TODO: Use .get() method to return None if account doesn't exist

    def transfer(self, from_account_number, to_account_number, amount):
        # TODO: Get from_account and to_account using get_account method
        from_account = self.get_account(from_account_number)
        to_account = self.get_account(to_account_number)
        # TODO: Check if both accounts exist
        # TODO: If either account not found, return (False, "One or both accounts not found")
        if from_account is None  or to_account is None:
            return False, "One or both accounts  not found"

        # TODO: Try to withdraw amount from from_account
        success, message = from_account.widthraw(amount)
        # TODO: If withdrawal fails, return (False, f"Transfer failed: {message}")
        if not success:
            return False, f"Transfer failed: {message}"
        
        # TODO: If withdrawal succeeds, deposit amount to to_account
        # TODO: Return (True, f"Transferred ${amount:.2f} from {from_account_number} to {to_account_number}")
        return True, f"Transferred $ {amount:.2f} from {from_account_number} to {to_account_number}"
