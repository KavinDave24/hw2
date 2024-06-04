"""This is the starting test file"""
from calculator import Calculator


def test_calculator_operations():
    """Bunch of calculator class tests"""
    assert Calculator.add(2, 2) == 4, "The Addition Function Failed"
    assert Calculator.divide(2, 2) == 1, "The Division Function Failed"
    assert Calculator.multiply(2, 2) == 4, "Multiplication Didn't work"
    assert Calculator.subtract(2, 2) == 0,  "subtraction didn't work"
