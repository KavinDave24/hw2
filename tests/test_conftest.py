
import pytest
from faker import Faker
from calculator import Calculator

faker = Faker()


def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=10, type=int,
                     help="Number of records to generate for tests")


@pytest.fixture
def num_records(request):
    return request.config.getoption("--num_records")


def generate_fake_data(num_records):
    data = []
    operations = ['add', 'subtract', 'multiply', 'divide']
    for _ in range(num_records):
        a = faker.random_number(digits=2)
        b = faker.random_number(digits=2)
        operation = faker.random_choice(elements=operations)
        if operation == 'add':
            result = Calculator.add(a, b)
        elif operation == 'subtract':
            result = Calculator.subtract(a, b)
        elif operation == 'multiply':
            result = Calculator.multiply(a, b)
        elif operation == 'divide':
            if b == 0:
                result = "Cannot divide by zero"
            else:
                result = Calculator.divide(a, b)
        data.append((a, b, operation, result))
    return data


@pytest.fixture
def fake_data(num_records):
    return generate_fake_data(num_records)
