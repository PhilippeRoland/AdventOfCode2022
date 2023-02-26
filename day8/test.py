import unittest
import core
from utils import read_file

class Day8Test(unittest.TestCase):
    def test_solution(self):
        lines = read_file('test_input')
        self.assertEqual(42, core.solution(lines))

if __name__ == '__main__':
    unittest.main()
