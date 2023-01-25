import unittest
import core
from utils import read_file


class Day7Test(unittest.TestCase):

    def test_calc_size(self):
        lines = read_file('test_input_1')
        self.assertEqual(2000, core.solution(lines))

    def test_solution(self):
        lines = read_file('test_input')
        self.assertEqual(95437, core.solution(lines))


if __name__ == '__main__':
    unittest.main()