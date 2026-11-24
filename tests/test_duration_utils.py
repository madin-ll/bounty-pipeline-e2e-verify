import unittest

from duration_utils import parse_duration


class ParseDurationTests(unittest.TestCase):
    def test_weeks(self) -> None:
        self.assertEqual(parse_duration("1w"), 604800)

    def test_combined(self) -> None:
        self.assertEqual(parse_duration("1h30m"), 5400)

    # --- regression: the 'd' unit used to be missing from the unit table and
    # was silently skipped, so '1d' returned 0 and '2d4h' returned 14400.
    def test_days(self) -> None:
        self.assertEqual(parse_duration("1d"), 86400)

    def test_days_and_hours(self) -> None:
        self.assertEqual(parse_duration("2d4h"), 187200)

    def test_all_units(self) -> None:
        self.assertEqual(parse_duration("1w2d3h4m5s"), 604800 + 2 * 86400 + 3 * 3600 + 4 * 60 + 5)
        self.assertEqual(parse_duration("1w2d3h4m5s"), 788645)

    def test_week_plus_day(self) -> None:
        self.assertEqual(parse_duration("1w1d"), 691200)

    def test_zero_amounts(self) -> None:
        self.assertEqual(parse_duration("0d"), 0)
        self.assertEqual(parse_duration("0s"), 0)

    def test_whitespace_tolerated(self) -> None:
        self.assertEqual(parse_duration(" 1d "), 86400)
        self.assertEqual(parse_duration("2d 4h"), 187200)

    def test_empty(self) -> None:
        self.assertEqual(parse_duration(""), 0)
        self.assertEqual(parse_duration("   "), 0)

    # --- invalid specs are rejected instead of being silently mis-parsed.
    def test_unknown_unit_rejected(self) -> None:
        for spec in ("1y", "5x", "1D", "abc", "d", "1", "-1d", "1d1"):
            with self.subTest(spec=spec), self.assertRaises(ValueError):
                parse_duration(spec)

    def test_repeated_unit_rejected(self) -> None:
        with self.assertRaises(ValueError):
            parse_duration("1h2h")

    def test_out_of_order_rejected(self) -> None:
        for spec in ("30m1h", "1s1d", "1m1w"):
            with self.subTest(spec=spec), self.assertRaises(ValueError):
                parse_duration(spec)

    def test_non_string_rejected(self) -> None:
        with self.assertRaises(ValueError):
            parse_duration(None)  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
