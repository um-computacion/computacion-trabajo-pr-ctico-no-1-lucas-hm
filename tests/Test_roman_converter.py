import unittest
from src.roman_converter import decimal_to_roman

class TestRomanConverter(unittest.TestCase):
    def test_decimal_to_roman(self):
        self.assertEqual(decimal_to_roman.decimal_to_roman(1), "I")
        self.assertEqual(decimal_to_roman.decimal_to_roman(4), "IV")
        self.assertEqual(decimal_to_roman.decimal_to_roman(9), "IX")
        self.assertEqual(decimal_to_roman.decimal_to_roman(58), "LVIII")
        self.assertEqual(decimal_to_roman.decimal_to_roman(1994), "MCMXCIV")

    def test_from_roman(self):
        self.assertEqual(decimal_to_roman.from_roman("I"), 1)
        self.assertEqual(decimal_to_roman.from_roman("IV"), 4)
        self.assertEqual(decimal_to_roman.from_roman("IX"), 9)
        self.assertEqual(decimal_to_roman.from_roman("LVIII"), 58)
        self.assertEqual(decimal_to_roman.from_roman("MCMXCIV"), 1994)

    def test_edge_cases(self):
        self.assertEqual(decimal_to_roman.from_roman("MMMCMXCIX"), 3999)
        self.assertEqual(decimal_to_roman.decimal_to_roman(3999), "MMMCMXCIX")

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            decimal_to_roman.decimal_to_roman(0)
        with self.assertRaises(ValueError):
            decimal_to_roman.from_roman("IIII")
        with self.assertRaises(ValueError):
            decimal_to_roman.from_roman("ABC")

if __name__ == "__main__":
    unittest.main()