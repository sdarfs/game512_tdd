import unittest

from main import *


class Test_game512(unittest.TestCase):
    def test_number_from_index_1(self):
        self.assertEqual(get_number_from_index(1, 2), 7)

    def test_number_from_index_2(self):
        self.assertEqual(get_number_from_index(3, 3), 16)

    def test_get_index_from_number_1(self):
        self.assertEqual(get_index_from_number(16), (3, 3))

    def test_get_index_from_number_2(self):
        self.assertEqual(get_index_from_number(1), (0, 0))

    def test_get_index_from_number_3(self):
        self.assertEqual(get_index_from_number(5), (1, 0))

    def test_zero_in_mas_1(self):
        mas = [
            [1, 1, 1, 1],
            [1, 1, 0, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
        ]
        self.assertEqual(zero_in_mas(mas), True)

    def test_zero_in_mas_2(self):
        mas = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
        ]
        self.assertEqual(zero_in_mas(mas), False)
