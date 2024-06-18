import pytest

from operations import operations, Calculator
from history import History



def test_calculator_operations(fake_data):
    """Test calculator operations with generated data"""
    for a, b, operation, expected in fake_data:
        if operation == 'add':
            assert Calculator.add(a, b) == expected, f"Failed on addition with {a} + {b}"
        elif operation == 'subtract':
            assert Calculator.subtract(a, b) == expected, f"Failed on subtraction with {a} - {b}"
        elif operation == 'multiply':
            assert Calculator.multiply(a, b) == expected, f"Failed on multiplication with {a} * {b}"
        elif operation == 'divide':
            if b == 0:
                with pytest.raises(ValueError, match="Cannot divide by zero"):
                    Calculator.divide(a, b)
            else:
                assert Calculator.divide(a, b) == expected, f"Failed on division with {a} / {b}"
