import unittest
from math_tools import is_prime

class TestMathLogic(unittest.TestCase):
    def test_prime(self):
        # Verification: 7 is prime, 4 is not
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(4))

if __name__ == "__main__":
    unittest.main()