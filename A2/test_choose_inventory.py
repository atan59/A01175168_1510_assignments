from unittest import TestCase
from unittest.mock import patch
from A2.dungeonsanddragons import choose_inventory


class TestChoose_inventory(TestCase):
    @patch('builtins.input', return_value=-1)
    def test_choose_inventory_buy_nothing(self, mock_input):
        expected = []
        actual = choose_inventory(['The Fantastic Plane Tradepost', 'Adamantine Armor', 'Demon Armor', 'Dwarven Plate',
                                   'Mariner\'s Armor', 'Sentinel Shield', 'Spellguard Shield', 'Sun Blade',
                                   'Wand of Enemy Destruction', 'Javelin of Lightning'])
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[1, -1])
    def test_choose_inventory_buy_one_item(self, mock_input):
        expected = ['Adamantine Armor']
        actual = choose_inventory(['The Fantastic Plane Tradepost', 'Adamantine Armor', 'Demon Armor', 'Dwarven Plate',
                                   'Mariner\'s Armor', 'Sentinel Shield', 'Spellguard Shield', 'Sun Blade',
                                   'Wand of Enemy Destruction', 'Javelin of Lightning'])
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[1, 2, -1])
    def test_choose_inventory_buy_two_items(self, mock_input):
        expected = ['Adamantine Armor', 'Demon Armor']
        actual = choose_inventory(['The Fantastic Plane Tradepost', 'Adamantine Armor', 'Demon Armor', 'Dwarven Plate',
                                   'Mariner\'s Armor', 'Sentinel Shield', 'Spellguard Shield', 'Sun Blade',
                                   'Wand of Enemy Destruction', 'Javelin of Lightning'])
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=[1, 1, -1])
    def test_choose_inventory_buy_multiples_of_same_item(self, mock_input):
        expected = ['Adamantine Armor', 'Adamantine Armor']
        actual = choose_inventory(['The Fantastic Plane Tradepost', 'Adamantine Armor', 'Demon Armor', 'Dwarven Plate',
                                   'Mariner\'s Armor', 'Sentinel Shield', 'Spellguard Shield', 'Sun Blade',
                                   'Wand of Enemy Destruction', 'Javelin of Lightning'])
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value=-1)
    def test_choose_inventory_buy_nothing_check_if_list(self, mock_input):
        actual = choose_inventory(['The Fantastic Plane Tradepost', 'Adamantine Armor', 'Demon Armor', 'Dwarven Plate',
                                   'Mariner\'s Armor', 'Sentinel Shield', 'Spellguard Shield', 'Sun Blade',
                                   'Wand of Enemy Destruction', 'Javelin of Lightning'])
        self.assertEqual(type(actual), list)

    @patch('builtins.input', side_effect=[1, -1])
    def test_choose_inventory_buy_one_item_check_if_list(self, mock_input):
        actual = choose_inventory(['The Fantastic Plane Tradepost', 'Adamantine Armor', 'Demon Armor', 'Dwarven Plate',
                                   'Mariner\'s Armor', 'Sentinel Shield', 'Spellguard Shield', 'Sun Blade',
                                   'Wand of Enemy Destruction', 'Javelin of Lightning'])
        self.assertEqual(type(actual), list)

    @patch('builtins.input', side_effect=[1, 2, -1])
    def test_choose_inventory_buy_two_items_check_if_list(self, mock_input):
        actual = choose_inventory(['The Fantastic Plane Tradepost', 'Adamantine Armor', 'Demon Armor', 'Dwarven Plate',
                                   'Mariner\'s Armor', 'Sentinel Shield', 'Spellguard Shield', 'Sun Blade',
                                   'Wand of Enemy Destruction', 'Javelin of Lightning'])
        self.assertEqual(type(actual), list)

    @patch('builtins.input', side_effect=[1, 1, -1])
    def test_choose_inventory_buy_multiples_of_same_item_check_if_list(self, mock_input):
        actual = choose_inventory(['The Fantastic Plane Tradepost', 'Adamantine Armor', 'Demon Armor', 'Dwarven Plate',
                                   'Mariner\'s Armor', 'Sentinel Shield', 'Spellguard Shield', 'Sun Blade',
                                   'Wand of Enemy Destruction', 'Javelin of Lightning'])
        self.assertEqual(type(actual), list)
