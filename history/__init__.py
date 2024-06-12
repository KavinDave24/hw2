class History(list):
    """
    This is the History class. It extends the built-in list class.
    """

    def __init__(self):
        """
        This is the constructor for the History class.
        """
        super().__init__()

    def get_last_result(self):
        """
        This method returns the result of the last calculation in the history.
        """
        if self:
            return self[-1].get_result()
        else:
            return None

    def print_history(self):
        """
        This method prints the history of calculations.
        """
        for i, calculation in enumerate(self, start=1):
            print(f"Calculation {i}: {calculation} = {calculation.get_result()}")
