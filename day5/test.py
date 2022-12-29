import unittest
import core
from utils import read_file, print_lines


class Day5Test(unittest.TestCase):

    def test_parse_input(self):
        lines = read_file('test_input')
        print_lines(lines)
        setup, instructions = core.parse_input(lines)
        self.assertEqual(2, len(setup[0]))
        self.assertEqual(3, len(setup[1]))
        self.assertEqual('D', setup[1][0])

    #def test_solution(self):
        #lines = read_file('test_input')
        #self.assertEqual(42, core.solution(lines))

if __name__ == '__main__':
    unittest.main()
