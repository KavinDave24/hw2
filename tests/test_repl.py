# tests/test_main.py

import pytest
from calculator.main import main  # Import your main application logic or entry point


def test_main_add_command(capfd):
    # Example: Test adding functionality through REPL
    with pytest.raises(SystemExit):
        input_values = iter(['add 2 3', 'exit'])
        main(input=input_values)

    out, _ = capfd.readouterr()
    assert "The result of 2 add 3 is equal to 5" in out


def test_main_subtract_command(capfd):

    with pytest.raises(SystemExit):
        input_values = iter(['subtract 5 2', 'exit'])
        main(input=input_values)

    out, _ = capfd.readouterr()
    assert "The result of 5 subtract 2 is equal to 3" in out


