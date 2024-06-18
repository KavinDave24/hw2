# tests/test_main.py
import pytest
from calculator import Calculator


@pytest.mark.parametrize("a, b, operation, expected", [
    ("5", "3", 'add', "The result of 5 add 3 is equal to 8"),
    ("10", "2", 'subtract', "The result of 10 subtract 2 is equal to 8"),
    ("4", "5", 'multiply', "The result of 4 multiply 5 is equal to 20"),
    ("20", "4", 'divide', "The result of 20 divide 4 is equal to 5"),
    ("1", "0", 'divide', "An error occurred: Cannot divide by zero"),
    ("9", "3", 'unknown', "Unknown operation: unknown"),
    ("a", "3", 'add', "Invalid number input: a or 3 is not a valid number."),
    ("5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number."),
])
def test_main(a, b, operation, expected, capsys):
    import main
    main.input = lambda prompt: a if "first" in prompt else b if "second" in prompt else operation
    main.main()
    captured = capsys.readouterr()
    assert expected in captured.out



from calculator.main import main

def test_main(monkeypatch):
    inputs = iter(["add 5 3", "subtract 10 2", "multiply 4 5", "divide 20 4", "divide 1 0", "unknown 9 3", "add a 3", "subtract 5 b", "exit"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()  # Run the REPL

# Ensure you have assertions or checks within the REPL to verify outputs or errors.
