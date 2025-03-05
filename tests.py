import unittest

from main import *


class Test_game512(unittest.TestCase):
    def test_number_from_index_1(self):
        self.assertEqual(get_number_from_index(1, 2), 7)

    def test_number_from_index_2(self):
        self.assertEqual(get_number_from_index(3, 3), 16)
