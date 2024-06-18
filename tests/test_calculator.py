# tests/test_calculator.py
from calculator import Calculator
from calculator.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand


def test_calculator_operations():
    assert Calculator.add(2, 3) == 5
    assert Calculator.subtract(5, 3) == 2
    assert Calculator.multiply(4, 5) == 20
    assert Calculator.divide(20, 4) == 5
    assert Calculator.divide(1, 0) == "Cannot divide by zero"

# tests/test_commands.py
import pytest
from calculator import commands

def test_add_command():
    command = AddCommand(3, 2)
    result = command.execute()
    assert result == 5

def test_subtract_command():
    command = SubtractCommand(3, 2)
    result = command.execute()
    assert result == 1

def test_multiply_command():
    command = MultiplyCommand(4, 5)
    result = command.execute()
    assert result == 20

def test_divide_command():
    command = DivideCommand(20, 4)
    result = command.execute()
    assert result == 5

def test_divide_by_zero():
    command = DivideCommand(1, 0)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        command.execute()
