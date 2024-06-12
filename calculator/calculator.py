class Calculator:
    @staticmethod
    def addition(x, y):
        return x + y

    @staticmethod
    def subtraction(x, y):
        return x - y

    @staticmethod
    def multiplication(x, y):
        return x * y

    @staticmethod
    def division(x, y):
        if y == 0:
            raise ValueError("Cannot divide by zero")
        return x / y


print(Calculator.subtract(5, 3))
