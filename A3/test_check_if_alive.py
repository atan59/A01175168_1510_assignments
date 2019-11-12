from unittest import TestCase
from A3.sud import check_if_alive


class TestCheckIfAlive(TestCase):
    def test_check_if_alive_true(self):
        expected = True
        actual = check_if_alive({'Name': 'Test', 'HP': [1, 10]})
        self.assertEqual(expected, actual)

    def test_check_if_alive_false(self):
        expected = False
        actual = check_if_alive({'Name': 'Test', 'HP': [0, 10]})
        self.assertEqual(expected, actual)

    def test_check_if_alive_true_type(self):
        expected = type(True)
        actual = type(check_if_alive({'Name': 'Test', 'HP': [1, 10]}))
        self.assertEqual(expected, actual)

    def test_check_if_alive_false_type(self):
        expected = type(False)
        actual = type(check_if_alive({'Name': 'Test', 'HP': [0, 10]}))
        self.assertEqual(expected, actual)
