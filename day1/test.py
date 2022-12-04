import unittest
import core
from utils import read_file


class Day1Test(unittest.TestCase):

    def test_split_lines(self):
        lines = read_file('test_input')
        self.assertEqual(5, len(core.split_cast_lines(lines)))

    def test_max_calories(self):
        self.assertEqual(24000, core.max_calories('test_input'))

    def test_top_three_calories(self):
        self.assertEqual(45000, core.sum_top_three_calories('test_input'))



if __name__ == '__main__':
    unittest.main()
