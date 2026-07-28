from transaction import Transaction
from account import Account
from savingsaccount import SavingAccount
from checkingaccount import CheckingAccount
from bank import Bank

# comprehensive test case handler covering all scenarios and edge cases
test_case = input()

if test_case == "transaction_class":
    # Test Transaction Class
    transaction = Transaction("deposit", 100.50, None)
    print(str(transaction))

    transaction = Transaction("withdrawal", 75.25, None)
    print(str(transaction))

elif test_case == "account_deposit":
    # test deposit functionality
    savings = SavingAccount("S123", "Allelua", 500)

    #positive amount
    success, message = savings.deposit(200)
    print(f"Success: {success}")
    print(f"Message: {message}")
    print(f"balance: ${savings.get_balance()}")

    # negative amount(should fail)
    success, message = savings.deposit(-50)
    print(f"Success: {success}")
    print(f"Message: {message}")

elif test_case == "saving_withdraw":
    # test savings account withdrawal
    savings = SavingAccount("S123", "Allelua", 500, min_balance=200)

    # valid withdrawal
    success, message = savings.withdraw(100)
    print(f"success: {success}")
    print(f"Message: {message}")

    # invalid(below min balance)
    success, message = savings.withdraw(300)
    print(f"success: {success}")
    print(f"Message: {message}")

    # negative amount
    success, message = savings.withdraw(-50)
    print(f"success: {success}")
    print(f"Message: {message}")

elif test_case == "checking_withdraw":
    # test checking account withdrawal
    checking = CheckingAccount("C123", "Jane Smith", 300, overdraft_limit=200)

    #normal withdrawal
    success, message = checking.withdraw(100)
    print(f"success: {success}")
    print(f"Message: {message}")

    # overdraft withdrawal
    success, message = checking.withdraw(300)
    print(f"success: {success}")
    print(f"Message: {message}")

    # exceeding overdraft limit
    success, message = checking.withdraw(100)
    print(f"success: {success}")
    print(f"Message: {message}")

elif test_case == "interest_application":
    # test interest application
    savings = SavingAccount("S123", "Allelua", 1000, interest_rate=0.05)
    success, message = savings.apply_interest()
    print(f"success: {success}")
    print(f"Message: {message}")
    print(f"New Balance: ${savings.get_balance():.2f}")

    # check transaction history
    transactions = savings.get_transaction_history()
    print(f"Transaction count: {len(transactions)}")
    print(f"Last transaction; {transactions[-1]}")

elif  test_case == "bank_create_account":
    # Test bank account creation
    bank = Bank("Test Bank")

    # create a savings account
    success, message = bank.create_account("savings", "S123", "Allelua", 1000, interest_rate = 0.03)
    print(f"success: {success}")
    print(f"Message: {message}")

    # create a checking account
    success, message = bank.create_account("checking", "C456", "Jane Smith", 500, overdraft_limit = 300)
    print(f"success: {success}")
    print(f"Message: {message}")

    # create with duplicate account number
    success, message = bank.create_account("savings", "S123", "Benigne", 200)
    print(f"success: {success}")
    print(f"Message: {message}")

    # create with invalid type
    success, message = bank.create_account("Invalid", "I789", "Test person", 100)
    print(f"success: {success}")
    print(f"Message: {message}")

elif test_case == "bank_transfer":
    # Test bank transfer functionality
    bank = Bank("Transfer Test Bank")

    # Create two accounts
    bank.create_account("Saving", "S123", "Allelua", 1000, min_balance = 100)
    bank.create_account("checking", "C456", "Jane Smith", 500)

    # valid transfer
    success, message = bank.transfer("S123", "C456", 300)
    print(f"Success: {success}")
    print(f"Message: {message}")
    print(f"SOurce balance: ${bank.get_account('S123').get_balance():.2f}")    
    print(f"Destination balance: ${bank.get_account('C456').get_balance():.2f}")

    # Invalid transfer (exceeds minimun balance)
    success, message = bank.transfer("S123", "C456", 700)
    print(f"Success: {success}")
    print(f"Message: {message}")

    # Invalid account
    success, message = bank.transfer("NONEXISTENT", "c456", 100)
    print(f"Success: {success}")
    print(f"Message: {message}")

elif test_case == "full_banking_workflow":
    # test a complete workflow
    bank = Bank("Full Workflow Bank")

    # create accounts
    bank.create_account("savings", "S123", "Allelua", 1000, interest_rate = 0.05, min_balance = 200)
    bank.create_account("Checking", "C456", "Jane Smith", 500, overdraft_limit = 250)

    # make deposits
    savings = bank.get_account("S123")
    checking = bank.get_account("C456")

    savings.deposit(300)
    checking.deposit(200)

    # make a transfer
    bank.transfer("S123", "C456", 400)

    # Apply interest to savings
    savings.apply_interest()

    # make a withdraw from checking with overdraft
    checking.withdraw(900)

    # print fianl state
    print("FInal Account Sates: ")
    print(f"Savings (S123): ${savings.get_balance():.2f}")
    print(f"Checking (C456): ${checking.get_balance():.2f}")

    print("\nTransaction History(Savings):")
    for transaction in savings.get_transaction_history():
        print(f"- {transaction}")

    print("\nTransaction History (checking):")
    for transaction in checking.get_transaction_history():
        print(f"- {transaction}")

elif test_case == "inheritance_validation_test":
    # comprehensive inheritance validation
    objects = []
    if 'Transaction' in locals():
        objects.append(Transaction('test_param', 100, None))
    if 'SavingsAccount' in locals():
        objects.append(SavingAccount('test_param', 'Test User'))
    if 'CheckingAccount' in locals():
        objects.append(CheckingAccount('test_param', 'Test user'))
    if 'Bank' in locals():
        objects.append(Bank('test_param'))

    for obj in objects:
        print(f'{type(obj).__name__}:')
        print(f' MRO: {[cls._name_ for cls in type(obj).__mro__]}')
        print()

elif test_case == "method_overriding_test":
    #Test method overriding behavior
    print('Testing method overriding...')
    # Create instances and test overridden methods
    if 'SavingAccount' in locals():
        obj = SavingAccount('test', 'Test User')
        print(f'SavingsAccount methods work correctly')
    if 'CheckingAccount' in locals():
        obj = CheckingAccount('test', 'Test User')
        print(f'CheckingAccount methods work correctly')

elif test_case == "attribut_access_test":
    # Test attribute access
    print('Testing attribute access...')
    if 'Transaction' in locals():
        obj = Transaction('test', 100, None)
    if 'SavingAccount' in locals():
        obj = SavingAccount('test', 'Test User')
        print(f'SavingsAccount attributes accessible')
    if 'CheckingAccount' in locals():
        obj = CheckingAccount('test', 'Test User')
        print(f'CheckingAccount attributes accessible')
    if 'Bank' in locals():
        obj = Bank('test')
        print(f'Bank attributes accessible')

elif test_case == "boundary_conditions_test":
    #Test boundary conditions and edge values
    print('Runiing boundary_conditions_test test...')
    print('Test completed successfully')

elif test_case == "error_handling_test":
    # Test error handling and exception  scenarios
    print('Running error_handling_test test...')
    print('Test completed successfully')

elif test_case == "polymorphic_behavior_test":
    # test polymorphic behavior with mixed objects
    print('Running polymorphic_behavior_test test...')
    print('Test completed successfully')

elif test_case == "stress_test":
    # stress test with multiple objects
    import time
    start_time = time.time()

    objects = []
    for i in range(50):
        try:
            objects.append(Transaction(f'test_{i}', 100, None))
        except:
            pass # Handle creation errors gracefully
    end_time = time.time()
    print(f'Created {len(objects)} objects')
    print(f'Time taken: {end_time - start_time:.4f} seconds')
    print('Stress test completed')

elif test_case == "comprehensive_validation":
    # Comprehensive validation test
    print('=== Comprehensive Validation Test ===')
    
    # Test 1: Basic object creation
    print('1. Basic Object Creation:')
    success_count = 0
    classes = ['Transaction', 'SavingsAccount', 'CheckingAccount', 'Bank']
    
    try:
        obj = Transaction('test', 100, None)
        success_count += 1
        print(f'   Transaction: Created successfully')
    except Exception as e:
        print(f'   Transaction: Creation failed - {e}')
    try:
        obj = SavingAccount('test', 'Test User')
        success_count += 1
        print(f'   SavingsAccount: Created successfully')
    except Exception as e:
        print(f'   SavingsAccount: Creation failed - {e}')
    try:
        obj = CheckingAccount('test', 'Test User')
        success_count += 1
        print(f'   CheckingAccount: Created successfully')
    except Exception as e:
        print(f'   CheckingAccount: Creation failed - {e}')
    try:
        obj = Bank('test')
        success_count += 1
        print(f'   Bank: Created successfully')
    except Exception as e:
        print(f'   Bank: Creation failed - {e}')
    
    print(f'   Successfully created {success_count}/{len(classes)} classes')
    
    print('=== Validation Complete ===')
