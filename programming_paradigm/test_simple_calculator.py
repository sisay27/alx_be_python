import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_add(self):
        """Test the add method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(2, 5), -3)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_multiply(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(4, 3), 12)
        self.assertEqual(self.calc.multiply(-2, 5), -10)
        self.assertEqual(self.calc.multiply(0, 10), 0)

    def test_divide(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-12, 3), -4)
        self.assertEqual(self.calc.divide(0, 10), 0)
        # Test division by zero
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)


if __name__ == '__main__':
    unittest.main()