import unittest
from duration_utils import parse_duration

class ParseDurationTests(unittest.TestCase):
    def test_weeks(self) -> None:
        self.assertEqual(parse_duration("1w"), 604800)

    def test_days(self) -> None:
        self.assertEqual(parse_duration("1d"), 86400)

    def test_days_combined(self) -> None:
        self.assertEqual(parse_duration("2d4h"), 187200)

    def test_combined(self) -> None:
        self.assertEqual(parse_duration("1h30m"), 5400)

    def test_uppercase_units(self) -> None:
        self.assertEqual(parse_duration("1D2H"), 93600)

    def test_surrounding_whitespace(self) -> None:
        self.assertEqual(parse_duration(" 1D2H "), 93600)
