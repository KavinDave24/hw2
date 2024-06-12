class Calculation:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_result(self):
        raise NotImplementedError("Subclasses must implement get_result method")


class addition(Calculation):
    def get_result(self):
        return self.x + self.y


class subtraction(Calculation):
    def get_result(self):
        return self.x - self.y


class multiplication(Calculation):
    def get_result(self):
        return self.x * self.y


class division(Calculation):
    def get_result(self):
        if self.y == 0:
            raise ValueError("Cannot divide by zero")
        return self.x / self.y
