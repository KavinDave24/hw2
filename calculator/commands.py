# commands.py
from abc import ABC, abstractmethod
from calculator import Calculator


class Command(ABC):
    @abstractmethod
    def execute(self) -> float:
        pass


class AddCommand(Command):
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def execute(self) -> float:
        return Calculator.add(self.x, self.y)


class SubtractCommand(Command):
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def execute(self) -> float:
        return Calculator.subtract(self.x, self.y)


class MultiplyCommand(Command):
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def execute(self) -> float:
        return Calculator.multiply(self.x, self.y)


class DivideCommand(Command):
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def execute(self) -> float:
        return Calculator.divide(self.x, self.y)
