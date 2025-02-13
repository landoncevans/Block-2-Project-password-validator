import unittest
from PasswordChecker import isValid


class test(unittest.TestCase):
    def test_is_valid(self):
        self.assertTrue(isValid("A!dhtayionetsuvti83n"))

    def test_is_invalid(self):
        self.assertFalse(isValid("A!dhtayione"))
        self.assertFalse(isValid("Afdhtayionetsuvti83n"))
        self.assertFalse(isValid("e!dhtayionetsuvti83n"))


if __name__ == '__main__':
    unittest.main()
