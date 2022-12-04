import unittest
import core
from utils import read_file


class Days2Test(unittest.TestCase):
    def test_score(self):
        lines = read_file('test_input')
        moves_tuples = core.get_moves(lines)
        self.assertEqual(15, core.calc_score(moves_tuples))

    def test_score_bis(self):
        lines = read_file('test_input')
        moves_tuples = core.get_moves(lines)
        self.assertEqual(12, core.calc_score_bis(moves_tuples))


if __name__ == '__main__':
    unittest.main()
