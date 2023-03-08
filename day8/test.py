import unittest
import core
from utils import read_file

class Day8Test(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(Day8Test, self).__init__(*args, **kwargs)
        self.lines = read_file('test_input')

    def test_parse(self):
        tree_2d_list = core.parse_trees(self.lines)
        self.assertEqual(3, tree_2d_list[0][0])
        self.assertEqual(0, tree_2d_list[4][4])

    def test_is_visible(self):
        tree_2d_list = core.parse_trees(self.lines)
        self.assertTrue(core.is_visible(tree_2d_list, 0, 2))
        self.assertTrue(core.is_visible(tree_2d_list, 2, 0))
        self.assertTrue(core.is_visible(tree_2d_list, 4, 2))
        self.assertTrue(core.is_visible(tree_2d_list, 2, 4))
        self.assertTrue(core.is_visible(tree_2d_list, 1, 1))
        self.assertFalse(core.is_visible(tree_2d_list, 1, 3))

    def test_solution(self):
        self.assertEqual(21, core.solution(self.lines))

if __name__ == '__main__':
    unittest.main()
