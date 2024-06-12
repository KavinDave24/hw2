# tests/test_history_teacher.py
from calculator import addition
from calculator import multiplication
from history import History


def test_history_operations():
    addition_instance = addition(1, 2)
    assert addition_instance == 3

    history = History()
    history.append(addition_instance)
    assert len(history) == 1

    history.clear()
    assert len(history) == 0

    history.append(addition(1, 1))
    history.append(addition(1, 2))
    history.append(addition(1, 3))
    assert len(history) == 3

    retrieve_instance = history.pop(-1)
    assert retrieve_instance == 4
    assert len(history) == 2

    multiplication_instance1 = multiplication(2, 2)
    history.append(multiplication_instance1)
    assert len(history) == 3
    history.print_history()
