# app/repl.py
from commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand


def parse_input(user_input: str):
    parts = user_input.strip().split()
    if len(parts) != 3:
        raise ValueError("Invalid input format. Expected: <operation> <num1> <num2>")

    operation, num1, num2 = parts[0], float(parts[1]), float(parts[2])

    if operation == 'add':
        return AddCommand(num1, num2)
    elif operation == 'subtract':
        return SubtractCommand(num1, num2)
    elif operation == 'multiply':
        return MultiplyCommand(num1, num2)
    elif operation == 'divide':
        return DivideCommand(num1, num2)
    else:
        raise ValueError(f"Unknown operation: {operation}")


def repl():
    print("Welcome to the Calculator REPL. Type 'exit' to quit.")
    while True:
        try:
            user_input = input(">> ")
            if user_input.lower() == 'exit':
                break
            command = parse_input(user_input)
            result = command.execute()
            print(f"The result is: {result}")
        except Exception as e:
            print(f"Error: {e}")
