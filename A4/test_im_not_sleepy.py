from unittest import TestCase
from unittest.mock import patch
from A4.question_8 import im_not_sleepy
import io


class TestIm_not_sleepy(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_im_not_sleepy_output(self, mock_stdout):
        im_not_sleepy()
        actual = mock_stdout.getvalue()
        expected = "10:08 requires the most bars. It requires: 21 bars to display.\n"

    def test_im_not_sleepy_type(self):
        actual = type(im_not_sleepy())
        expected = type("10:08 requires the most bars. It requires: 21 bars to display.\n")
        self.assertEqual(expected, actual)
