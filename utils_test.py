import unittest
from utils import Utils

class TestUtils(unittest.TestCase):

    def test_reversed_with_integer_input(self):
        self.assertEqual(Utils.reversed(75848), 84857)

    def test_reversed_with_float_input(self):
        with self.assertRaises(TypeError):
            Utils.reversed(87.234)

    def test_reversed_with_string_input(self):
        with self.assertRaises(TypeError):
            Utils.reversed("hdkfhdfh")

    def test_formatter_with_integer_input(self):
        binary, octal = Utils.formatter(78)
        self.assertEqual(binary, "0b1001110")
        self.assertEqual(octal, "0o116")

    def test_formatter_with_float_input(self):
        with self.assertRaises(TypeError):
            Utils.formatter(348934.2434)

    def test_formatter_with_string_input(self):
        with self.assertRaises(TypeError):
            Utils.formatter("not a number")

if __name__ == '__main__':
    unittest.main()
