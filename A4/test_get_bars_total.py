from unittest import TestCase
from A4.question_8 import get_bars_total


class TestGetBarsTotal(TestCase):
    def test_get_bars_total_lowest_time(self):
        actual = get_bars_total(1, 0, 0)
        expected = 14
        self.assertEqual(expected, actual)

    def test_get_bars_total_highest_time(self):
        actual = get_bars_total(12, 5, 9)
        expected = 18
        self.assertEqual(expected, actual)

    def test_get_bars_total_lowest_bars(self):
        actual = get_bars_total(1, 1, 1)
        expected = 6
        self.assertEqual(expected, actual)

    def test_get_bars_total_highest_bars(self):
        actual = get_bars_total(10, 0, 8)
        expected = 21
        self.assertEqual(expected, actual)
