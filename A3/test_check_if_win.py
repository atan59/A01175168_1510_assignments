from unittest import TestCase
from A3.sud import check_if_win


class TestCheckIfWin(TestCase):
    def test_check_if_win_true(self):
        expected = True
        actual = check_if_win(5)
        self.assertEqual(expected, actual)

    def test_check_if_win_false(self):
        expected = False
        actual = check_if_win(0)
        self.assertEqual(expected, actual)

    def test_check_if_win_true_type(self):
        expected = type(True)
        actual = type(check_if_win(5))
        self.assertEqual(expected, actual)

    def test_check_if_win_false_type(self):
        expected = type(False)
        actual = type(check_if_win(0))
        self.assertEqual(expected, actual)
