from unittest import TestCase
from unittest.mock import patch
from A4.question_4 import selection_sort
import io


class TestSelectionSort(TestCase):
    def test_selection_sort_all_integers(self):
        actual = selection_sort(['2', '1', '5', '4', '3', '6'])
        expected = ['1', '2', '3', '4', '5', '6']
        self.assertEqual(expected, actual)

    def test_selection_sort_all_floats(self):
        actual = selection_sort(['2.3', '2.7', '5.1', '5.9', '4.2', '1.3'])
        expected = ['1.3', '2.3', '2.7', '4.2', '5.1', '5.9']
        self.assertEqual(expected, actual)

    def test_selection_sort_all_strings(self):
        actual = selection_sort(['e', 'a', 'c', 'd', 'b', 'f'])
        expected = ['a', 'b', 'c', 'd', 'e', 'f']
        self.assertEqual(expected, actual)

    def test_selection_sort_integers_and_floats(self):
        actual = selection_sort(['2', '1.3', '5.3', '4', '2.3', '6'])
        expected = ['1.3', '2', '2.3', '4', '5.3', '6']
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_selection_sort_empty_list(self, mock_stdout):
        selection_sort([])
        actual = mock_stdout.getvalue()
        expected = "Error: Empty list is not a valid value.\n"
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_selection_sort_unsortable_list(self, mock_stdout):
        selection_sort(['2', 'a'])
        actual = mock_stdout.getvalue()
        expected = ""
        self.assertEqual(expected, actual)
