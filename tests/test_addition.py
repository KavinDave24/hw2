# Inside app/calculations/__init__.py or another Python file in app.calculations
class Addition:
    def __init__(self, a=1, b=2):
        self.a = a
        self.b = b

    def calculate(self):
        return self.a + self.b
