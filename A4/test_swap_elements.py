from unittest import TestCase
from A4.question_4 import swap_elements


class TestSwapElements(TestCase):
    def test_swap_elements_already_in_order_strings(self):
        actual = swap_elements(['a', 'b', 'e', 'c'], 0)
        expected = ['a', 'b', 'e', 'c']
        self.assertEqual(expected, actual)

    def test_swap_elements_lowest_at_end_strings(self):
        actual = swap_elements(['z', 'b', 'e', 'a'], 0)
        expected = ['a', 'z', 'e', 'b']
        self.assertEqual(expected, actual)

    def test_swap_elements_lowest_next_to_index_strings(self):
        actual = swap_elements(['b', 'a', 'e', 'c'], 0)
        expected = ['a', 'b', 'e', 'c']
        self.assertEqual(expected, actual)

    def test_swap_elements_already_in_order_numbers(self):
        actual = swap_elements([1, 2, 4, 3], 0)
        expected = [1, 2, 4, 3]
        self.assertEqual(expected, actual)

    def test_swap_elements_lowest_at_end_numbers(self):
        actual = swap_elements([3, 2, 4, 1], 0)
        expected = [1, 3, 4, 2]
        self.assertEqual(expected, actual)

    def test_swap_elements_lowest_next_to_index_numbers(self):
        actual = swap_elements([2, 1, 4, 3], 0)
        expected = [1, 2, 4, 3]
        self.assertEqual(expected, actual)
