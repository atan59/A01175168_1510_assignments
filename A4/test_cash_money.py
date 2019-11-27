from unittest import TestCase
from unittest.mock import patch
from A4.question_5 import cash_money
import io


class TestCashMoney(TestCase):
    def test_cash_money_all_currency(self):
        actual = cash_money(188.41)
        expected = {100: 1, 50: 1, 20: 1, 10: 1, 5: 1, 2: 1, 1: 1, 0.25: 1, 0.1: 1, 0.05: 1, 0.01: 1}
        self.assertEqual(expected, actual)

    def test_cash_money_only_hundreds(self):
        actual = cash_money(100.00)
        expected = {100: 1}
        self.assertEqual(expected, actual)

    def test_cash_money_only_fifties(self):
        actual = cash_money(50.00)
        expected = {50: 1}
        self.assertEqual(expected, actual)

    def test_cash_money_only_twenties(self):
        actual = cash_money(20.00)
        expected = {20: 1}
        self.assertEqual(expected, actual)

    def test_cash_money_only_tens(self):
        actual = cash_money(10.00)
        expected = {10: 1}
        self.assertEqual(expected, actual)

    def test_cash_money_only_fives(self):
        actual = cash_money(5.00)
        expected = {5: 1}
        self.assertEqual(expected, actual)

    def test_cash_money_only_toonies(self):
        actual = cash_money(2.00)
        expected = {2: 1}
        self.assertEqual(expected, actual)

    def test_cash_money_only_loonies(self):
        actual = cash_money(1.00)
        expected = {1: 1}
        self.assertEqual(expected, actual)

    def test_cash_money_only_quarters(self):
        actual = cash_money(0.75)
        expected = {0.25: 3}
        self.assertEqual(expected, actual)

    def test_cash_money_only_dimes(self):
        actual = cash_money(0.20)
        expected = {0.1: 2}
        self.assertEqual(expected, actual)

    def test_cash_money_only_nickels(self):
        actual = cash_money(0.05)
        expected = {0.05: 1}
        self.assertEqual(expected, actual)

    def test_cash_money_only_pennies(self):
        actual = cash_money(0.04)
        expected = {0.01: 4}
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_cash_money_negative(self, mock_stdout):
        cash_money(-1.00)
        actual = mock_stdout.getvalue()
        expected = "Error: This is not a valid amount!\n"
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_cash_money_not_float(self, mock_stdout):
        cash_money("Hi")
        actual = mock_stdout.getvalue()
        expected = "Error: '<' not supported between instances of 'str' and 'int'\n"
        self.assertEqual(expected, actual)
