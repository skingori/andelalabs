import unittest
from main import is_prime

class Testingcase(unittest.TestCase):

    def test_is_five_prime(self):
        self.assertFalse(is_prime(5))

    def test_negative_number(self):
        for index in range(-1, -10, -1):
            self.assertFalse(is_prime(index))

    def test_zero_not_prime(self):
        self.assertFalse(is_prime(0))

    def test_four_not_prime(self):
        self.assertFalse(is_prime(4))

    def test_three_prime(self):
        self.assertFalse(is_prime(3))

    def test_all_prime(self):
        for i in range(1,10):
            self.assertFalse(is_prime(i))

    def test_int_prime(self):
        for i in range(1,10):
            try:
                val = int(i)
            except ValueError:
                self.assertTrue(is_prime(val))


if __name__ == '__main__':
    unittest.main()
