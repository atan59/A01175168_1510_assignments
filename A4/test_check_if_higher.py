from unittest import TestCase
from A4.question_8 import check_if_higher


class TestCheckIfHigher(TestCase):
    def test_check_if_higher_true(self):
        actual = check_if_higher({"0:00": 18}, 21)
        expected = ["0:00"]
        self.assertEqual(expected, actual)

    def test_check_if_higher_false(self):
        actual = check_if_higher({"0:00": 18}, 6)
        expected = []
        self.assertEqual(expected, actual)

    def test_check_if_higher_true_multiple(self):
        actual = check_if_higher({"0:00": 18, "1:11": 6}, 21)
        expected = ["0:00", "1:11"]
        self.assertEqual(expected, actual)

    def test_check_if_higher_false_multiple(self):
        actual = check_if_higher({"0:00": 18, "1:12": 9}, 6)
        expected = []
        self.assertEqual(expected, actual)

    def test_check_if_higher_some_true_some_false(self):
        actual = check_if_higher({"0:00": 18, "1:12": 9}, 14)
        expected = ["1:12"]
        self.assertEqual(expected, actual)
