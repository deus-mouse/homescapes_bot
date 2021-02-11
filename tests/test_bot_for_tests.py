import unittest
import cv2 as cv

from unittest.mock import Mock
from PIL import Image
# import bot_class
from bot_for_tests import BotPuzzleSolver



_test_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 4, 1, 3, 3, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 5, 1, 5, 1, 4, 3, 0, 0, 0, 0],
                [0, 0, 0, 0, 5, 4, 2, 5, 4, 3, 0, 0, 0, 0],
                [0, 0, 0, 3, 2, 3, 1, 5, 5, 1, 3, 0, 0, 0],
                [0, 0, 0, 5, 3, 3, 0, 0, 3, 3, 1, 0, 0, 0],
                [0, 0, 0, 2, 4, 4, 3, 2, 4, 1, 2, 0, 0, 0],
                [0, 0, 0, 0, 1, 1, 3, 5, 3, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 3, 3, 2, 4, 3, 2, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]



path_what = 'tests/needles/test_full_window_region.png'
path_where = '/Users/roman/Documents/Documents_iMac/CodeProjects/PythonProjects/Homescapes_bot/needles/crops'

class TestBot(unittest.TestCase):

    def test_matrix_setter(self):
        test_bot = BotPuzzleSolver()
        test_bot.full_table_img_path = path_what
        test_bot.cropper(path_what=path_what, path_where=path_where)
        result = test_bot.matrix_setter(path_where)
        self.assertEqual(result, _test_matrix)

    # def test_searching_best_match(self):
    #     pass


if __name__ == '__main__':
    unittest.main()



