
class History(list):
    def __init__(self):
        super().__init__()

    def get_last_result(self):
        if self:
            return self[-1].get_result()
        else:
            return None

    def print_history(self):
        for i, calculation in enumerate(self, start=1):
            print(f"Calculation {i}: {calculation} = {calculation.get_result()}")
