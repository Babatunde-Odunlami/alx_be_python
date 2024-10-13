# mastering static method and class methods
class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Returns the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Returns the product of two numbers, printing the calculation type."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

