# main.py
from calculator import Calculator

def main():
    while True:
        try:
            a = input("Enter first number: ")
            b = input("Enter second number: ")
            operation = input("Enter operation (add, subtract, multiply, divide): ")

            a = float(a)
            b = float(b)

            if operation == 'add':
                result = Calculator.add(a, b)
            elif operation == 'subtract':
                result = Calculator.subtract(a, b)
            elif operation == 'multiply':
                result = Calculator.multiply(a, b)
            elif operation == 'divide':
                result = Calculator.divide(a, b)
            else:
                print(f"Unknown operation: {operation}")
                continue

            print(f"The result of {a} {operation} {b} is equal to {result}")

        except ValueError as e:
            print(f"An error occurred: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
