import unittest
from simple_calculator import SimpleCalculator
class TestSimpleCalculator(unittest.TestCase):
    def test_add(self):
        calculator = SimpleCalculator()
        result = calculator.add(2,3)
        self.assertEqual(result,5)
    def test_subtract(self):
        calculator = SimpleCalculator()
        result = calculator.subtract(5,2)
        self.assertEqual(result,3)

    def test_multiply(self):
        calculator = SimpleCalculator()
        result = calculator.multiply(2,3)
        self.assertEqual(result,6)
    def test_divide(self):
        calculator = SimpleCalculator()
        result = calculator.devide(6,2)
        self.assertEqual(result,3)
        with self.assertraises(ZeroDivisionError):
            calculator.devide(10,0)

if __name__== "__main__" :
    unittest.main()
