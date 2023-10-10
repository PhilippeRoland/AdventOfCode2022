import unittest
import core
from utils import read_file

class DayXTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(DayXTest, self).__init__(*args, **kwargs)
        self.lines = read_file('test_input')

    def test_solution(self):
        self.assertEqual(42, core.solution(self.lines))

    def test_solution_2(self):
        self.assertEqual(42, core.solution_2(self.lines))

if __name__ == '__main__':
    unittest.main()
