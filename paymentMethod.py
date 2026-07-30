from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self):
        pass
    @abstractmethod
    def payment_details(self):
        pass
    def validate(self, amount):
        if amount > 0:
            return True
        return False

class CreditCard(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number

    def process_payment(self, amount):
        return f"Processing credit card payment of ${amount}"

    def payment_details(self):
        # - Extracts the last 4 digits of the card number
        # - Masks the rest of the digits with asterisks (*)
        # - Returns a string in format: "Credit Card: [masked_number]"
        # - Example: "1234567890123456" becomes "************3456"
        print("Credit Card: ", end="")
        for number in self.card_number[:-4]:
            print("*", end="")
        print(self.card_number[-4:])
class PayPal(PaymentMethod):
    def __init__(self, email):
        self.email = email

    def process_payment(self, amount):
        return f"Processing PayPal payment of ${amount}"
    def payment_details(self):
        return f"PayPal account: {self.email}"

cc = CreditCard("1234567890123456")
pp = PayPal("user@gmail.com")

if cc.validate(100):
    print(cc.process_payment(100))
    cc.payment_details()

if pp.validate(200):
    print(pp.process_payment(200))
    print(pp.payment_details())