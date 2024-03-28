import unittest
from mathFunctions import MathFunctions as mf

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(mf.add(14, 12), 26)

    def test_subtract(self):
        self.assertEqual(mf.subtract(38, 23), 15)

    def test_multiply(self):
        self.assertEqual(mf.multiply(17, 32), 544)

    def test_divide(self):
        self.assertEqual(mf.divide(28, 4), 7)

if __name__ == '__main__':
    unittest.main()