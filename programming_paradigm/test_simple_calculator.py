import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Create a SimpleCalculator instance for testing."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(-1, -1), 0)

    def test_multiply(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-1, 5), -5)
        self.assertEqual(self.calc.multiply(0, 10), 0)

    def test_divide(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(5, 0), None)
        self.assertEqual(self.calc.divide(-10, -2), 5)
        self.assertEqual(self.calc.divide(0, 1), 0)
        self.assertEqual(self.calc.divide(2,"a"), None)
        self.assertEqual(self.calc.divide("a", 2), None)

if __name__ == '__main__':
    unittest.main()

