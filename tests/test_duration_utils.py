import unittest
from duration_utils import parse_duration


class ParseDurationTests(unittest.TestCase):
    def test_weeks(self) -> None:
        self.assertEqual(parse_duration('1w'), 604800)

    def test_days(self) -> None:
        self.assertEqual(parse_duration('1d'), 86400)
        self.assertEqual(parse_duration('2d4h'), 187200)

    def test_combined(self) -> None:
        self.assertEqual(parse_duration('1h30m'), 5400)
