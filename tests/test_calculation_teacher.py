from operations import Calculator


def test_calculator_operations():
    """Basic Calculator Tests using the Instance"""
    assert Calculator.addition(2, 2) == 4, "The Addition Function Failed"
    assert Calculator.division(2, 2) == 1, "The Division Function Failed"
    assert Calculator.multiplication(2, 2) == 4, "Multiplication Didn't work"
    assert Calculator.subtraction(2, 2) == 0, "subtraction didn't work"
