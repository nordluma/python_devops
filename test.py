import unittest

from calculations import add, multiply, power


class TestCalculations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(4, 5), 9, "The sum is wrong")

    def test_mult(self):
        self.assertEqual(multiply(9, 3), 27, "Multiplication failed")

    def test_pow(self):
        self.assertEqual(power(10, 2), 100, "The pow is wrong")


if __name__ == "__main__":
    unittest.main()
