class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, number):
        self.result += number
        return self.result
    
    def substract(self, number):
        self.result -= number
        return self.result
    
    def multiply(self, number):
        self.result *= number
        return self.result
    
    def divide(self,number):
        if number == 0:
            print("Error: Division by zero")
            return self.result
        self.result /= number
        return self.result

    def clear(self):
        self.result = 0

    def get_result(self):
        return f"The current result: {self.result}"

print("1. Test Initial result")
print("2. Addition")
print("3. Substraction")
print("4. Multiplication")
print("5. Division")
print("6. Clear")
print("7. Exit")



while True:
    choice = input("Enter number of your choice: ")
    choice = int(choice)
    if choice == 1:
        calc = Calculator()
        print(f"Initial result: {calc.get_result()}")

    elif choice == 2:
        calc = Calculator()
        result1 = calc.add(10)
        print(f"After adding 10: {result1}")
        result2 = calc.add(30)
        print(f"After adding 30: {result2}")
        print(f"Final result: {calc.get_result()}")

    elif choice == 3:
        calc = Calculator()
        calc.add(5)
        result1 = calc.multiply(4)
        print(f"After multiplying by 4: {result1}")
        result2 = calc.multiply(2)
        print(f"After multiplying by 2: {result2}")
        print(f"Final result: {calc.get_result()}")

    elif choice == 4:
        calc = Calculator()
        calc.add(100)
        result1 = calc.divide(4)
        print(f"After dividing by 4: {result1}")
        result2 = calc.divide(0)
        print(f"After dividing by 0: {result2}")
        print(f"Final result: {calc.get_result()}")

    elif choice == 5:
        calc = Calculator()
        calc.add(25)
        calc.multiply(3)
        print(f"Before clear: {calc.get_result()}")

        result = calc.clear()
        print(f"After clear: {result}")
        print(f"Current result: {calc.get_result()}")

    elif choice == 6:
        print("Exit. Byeeeee!!!!!!!!!!!!!!!!!!!!!!")
        break

    else:
        print("Invalid input")