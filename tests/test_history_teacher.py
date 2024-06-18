# tests/test_history_teacher.py
from calculator import Calculator
from history import History


def test_history_operations():
    addition_instance = Calculator.add(1, 2)
    assert addition_instance == 3, "Did not add 1 + 2 = 3"

    history = History()
    history.append(Calculator.add(1, 2))
    assert history[0] == 3, "History did not store the addition result"
    assert len(history) == 1, "History does not have one item"

    history.clear()
    assert len(history) == 0, "History did not clear"

    history.append(Calculator.add(1, 1))
    history.append(Calculator.add(1, 2))
    history.append(Calculator.add(1, 3))
    assert len(history) == 3, "History does not have three items"

    retrieved = history.pop(-1)
    assert retrieved == 4, "Retrieved item is not the last addition result"
    assert len(history) == 2, "History does not have two items after pop"

    history.append(Calculator.multiply(2, 2))
    assert len(history) == 3, "History does not have three items after adding multiplication"
    assert history[-1] == 4, "Last item in history is not the multiplication result"
    history.print_history()
