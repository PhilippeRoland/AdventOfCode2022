import unittest
import core
from utils import read_file


class Days3Test(unittest.TestCase):
    def test_score(self):
        lines = read_file('test_input')
        self.assertEqual(157, core.get_total_priority_of_duplicates(lines))

    def test_badges(self):
        lines = read_file('test_input')
        self.assertEqual(70, core.get_badges_priority(lines))

if __name__ == '__main__':
    unittest.main()
