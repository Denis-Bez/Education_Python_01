import unittest
import basic_calculator

class TestCalculator(unittest.TestCase):

    def test_additional(self):
        self.assertEqual(basic_calculator.addition(2, 2), 4)
        self.assertEqual(basic_calculator.addition(-2, 2), 0)
        self.assertEqual(basic_calculator.addition(-2, -2), -4)
    

    def test_substraction(self):
        self.assertEqual(basic_calculator.substraction(2, 2), 0)
        self.assertEqual(basic_calculator.substraction(-2, 2), -4)
        self.assertEqual(basic_calculator.substraction(-2, -2), 0)
    

    def test_multiplication(self):
        self.assertEqual(basic_calculator.multiplication(2, 2), 4)
        self.assertEqual(basic_calculator.multiplication(-2, 2), -4)
        self.assertEqual(basic_calculator.multiplication(-2, -2), 4)
    

    def test_division(self):
        self.assertEqual(basic_calculator.division(2, 2), 1)
        self.assertEqual(basic_calculator.division(-2, 2), -1)
        self.assertEqual(basic_calculator.division(1, 2), 0.5)

        with self.assertRaises(ValueError):
            basic_calculator.division(2, 0)
    

    def test_power(self):
        self.assertEqual(basic_calculator.power(2, 2), 4)
        self.assertEqual(basic_calculator.power(2, 0), 1)
        self.assertEqual(basic_calculator.power(0, 2), 0)

        with self.assertRaises(ValueError):
            basic_calculator.power(2, -2)
    

    def test_sqroot(self):
        self.assertEqual(basic_calculator.sqroot(4), 2)
        self.assertEqual(basic_calculator.sqroot(0), 0)

        with self.assertRaises(ValueError):
            basic_calculator.sqroot(-2)



# Running test from console: 'python -m unittest test_basic_calculator.py'
if __name__ == '__main__':
    unittest.main()