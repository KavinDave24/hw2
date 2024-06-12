"""This is the main startup of the app"""


def main():
    """This is the main function that is run"""


if __name__ == '__main__':
    """This causes the hello world function to be called if this is the __main__ top level of code"""
    main()


class Calculator:
    @staticmethod
    def addition(a, b):
        return a + b

    @staticmethod
    def subtraction(a, b):
        return a - b

    @staticmethod
    def multiplication(a, b):
        return a * b

    @staticmethod
    def division(a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b
