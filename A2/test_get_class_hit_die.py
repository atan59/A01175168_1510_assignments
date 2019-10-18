from unittest import TestCase
from A2.dungeonsanddragons import get_class_hit_die


class TestGetClassHitDie(TestCase):
    def test_get_class_hit_die_six(self):
        expected = 6
        actual = get_class_hit_die('sorcerer')
        self.assertEqual(expected, actual)

    def test_get_class_hit_die_eight(self):
        expected = 8
        actual = get_class_hit_die('bard')
        self.assertEqual(expected, actual)

    def test_get_class_hit_die_ten(self):
        expected = 10
        actual = get_class_hit_die('fighter')
        self.assertEqual(expected, actual)

    def test_get_class_hit_die_twelve(self):
        expected = 12
        actual = get_class_hit_die('barbarian')
        self.assertEqual(expected, actual)

    def test_get_class_hit_die_six_is_int(self):
        actual = get_class_hit_die('sorcerer')
        self.assertIs(type(actual), int)

    def test_get_class_hit_die_eight_is_int(self):
        actual = get_class_hit_die('bard')
        self.assertIs(type(actual), int)

    def test_get_class_hit_die_ten_is_int(self):
        actual = get_class_hit_die('fighter')
        self.assertIs(type(actual), int)

    def test_get_class_hit_die_twelve_is_int(self):
        actual = get_class_hit_die('barbarian')
        self.assertIs(type(actual), int)
