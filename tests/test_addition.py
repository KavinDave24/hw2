"""This is the starting test file"""
from calculator.addition import addition


def test_addition():
    """Add Two Numbers"""
    assert addition(2, 2) == 4, "Addition is not working"
