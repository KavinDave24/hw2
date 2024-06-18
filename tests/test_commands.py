# tests/test_commands.py
import pytest
from calculator.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from calculator import Calculator

class TestCommands:
    def setup_method(self):
        self.calculator = Calculator()

    def test_add_command(self):
        command = AddCommand(self.calculator, 3, 2)
        result = command.execute()
        assert result == 5, "AddCommand did not produce the correct result"

    def test_subtract_command(self):
        command = SubtractCommand(self.calculator, 3, 2)
        result = command.execute()
        assert result == 1, "SubtractCommand did not produce the correct result"

    def test_multiply_command(self):
        command = MultiplyCommand(self.calculator, 4, 5)
        result = command.execute()
        assert result == 20, "MultiplyCommand did not produce the correct result"

    def test_divide_command(self):
        command = DivideCommand(self.calculator, 20, 4)
        result = command.execute()
        assert result == 5, "DivideCommand did not produce the correct result"

    def test_divide_by_zero(self):
        command = DivideCommand(self.calculator, 1, 0)
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            command.execute()

if __name__ == "__main__":
    pytest.main()
