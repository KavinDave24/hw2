class Calculation:
    """
	This is the abstract Calculation class.
	"""

    def __init__(self, val1, val2):
        """
		This is the constructor for the Calculation class.
		"""
        self.val1 = val1
        self.val2 = val2

    def get_result(self):
        """
		This is the get_result method. It returns the result property.
		"""
        return self.result

    def set_result(self, result):
        """
		This is the set_result method. It sets the result property.
		"""
        self.result = result

    def get_val1(self):
        """
		This is the get_val1 method. It returns the val1 property.
		"""
        return self.val1

    def set_val1(self, val1):
        """
		This is the set_val1 method. It sets the val1 property.
		"""
        self.val1 = val1

    def get_val2(self):
        """
		This is the get_val2 method. It returns the val2 property.
		"""
        return self.val2

    def set_val2(self, val2):
        """
		This is the set_val2 method. It sets the val2 property.
		"""
        self.val2 = val2

    @classmethod
    def create_calculation(cls, val1, val2):
        """
		This is the create_calculation factory method. It creates and returns a Calculation object.
		"""
        return cls(val1, val2)


class Addition(Calculation):
    """
	This is the Addition class. It extends the Calculation class.
	"""

    def __init__(self, val1, val2):
        """
		This is the constructor for the Addition class.
		"""
        super().__init__(val1, val2)
        self.result = val1 + val2


class Subtraction(Calculation):
    """
	This is the Subtraction class. It extends the Calculation class.
	"""

    def __init__(self, val1, val2):
        """
		This is the constructor for the Subtraction class.
		"""
        super().__init__(val1, val2)
        self.result = val1 - val2


class Multiplication(Calculation):
    """
	This is the Multiplication class. It extends the Calculation class.
	"""

    def __init__(self, val1, val2):
        """
		This is the constructor for the Multiplication class.
		"""
        super().__init__(val1, val2)
        self.result = val1 * val2


class Division(Calculation):
    """
	This is the Division class. It extends the Calculation class.
	"""

    def __init__(self, val1, val2):
        """
		This is the constructor for the Division class.
		"""
        super().__init__(val1, val2)
        self.result = val1 / val2


if __name__ == "__main__":
    addition = Addition.create_calculation(2, 3)
    print(addition.get_result())
    subtraction = Subtraction.create_calculation(5, 2)
    print(subtraction.get_result())
    multiplication = Multiplication.create_calculation(4, 3)
    print(multiplication.get_result())
    division = Division.create_calculation(6, 2)
    print(division.get_result())
