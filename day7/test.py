import unittest
import core
from utils import read_file


class Day7Test(unittest.TestCase):

    def test_parse_tree(self):
        lines = read_file('test_input_1')
        tree = core.parse_tree(lines)
        self.assertEqual("/", tree.name)
        self.assertEqual(2000, tree.size)
        dir_a = tree.find_child('a')
        file_b = tree.find_child('b.txt')
        self.assertTrue(dir_a.children)
        self.assertFalse(file_b.children)
        file_f = dir_a.find_child('f')
        self.assertEqual(250, file_f.size)

    def test_solution_1(self):
        lines = read_file('test_input')
        self.assertEqual(95437, core.solution(lines))

    def test_solution_2(self):
        lines = read_file('test_input')
        self.assertEqual(24933642, core.solution_2(lines))

if __name__ == '__main__':
    unittest.main()
