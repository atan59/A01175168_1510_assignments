from unittest import TestCase
from unittest.mock import patch
from A4.question_3 import dijkstra
import io


class TestDijkstra(TestCase):
    def test_dijkstra_red_white_blue(self):
        colours_list = ['blue', 'white', 'blue', 'red', 'white']
        dijkstra(colours_list)
        actual = colours_list
        expected = ['red', 'white', 'white', 'blue', 'blue']
        self.assertEqual(expected, actual)

    def test_dijkstra_just_red_and_white(self):
        colours_list = ['white', 'red', 'white', 'red', 'white']
        dijkstra(colours_list)
        actual = colours_list
        expected = ['red', 'red', 'white', 'white', 'white']
        self.assertEqual(expected, actual)

    def test_dijkstra_just_red_and_blue(self):
        colours_list = ['blue', 'red', 'red', 'red', 'blue']
        dijkstra(colours_list)
        actual = colours_list
        expected = ['red', 'red', 'red', 'blue', 'blue']
        self.assertEqual(expected, actual)

    def test_dijkstra_just_white_and_blue(self):
        colours_list = ['blue', 'white', 'white', 'blue', 'blue']
        dijkstra(colours_list)
        actual = colours_list
        expected = ['white', 'white', 'blue', 'blue', 'blue']
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_dijkstra_empty_list(self, mock_stdout):
        colours_list = []
        dijkstra(colours_list)
        actual = mock_stdout.getvalue()
        expected = "Error: This is not a valid value!\n"
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_dijkstra_not_a_list(self, mock_stdout):
        colours_list = [1]
        dijkstra(colours_list)
        actual = mock_stdout.getvalue()
        expected = ""
        self.assertEqual(expected, actual)
