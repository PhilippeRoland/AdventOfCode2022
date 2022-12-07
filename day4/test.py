import unittest
import core
from utils import read_file

class Day4Test(unittest.TestCase):
    def test_solution(self):
        lines = read_file('test_input')
        self.assertEqual(2, core.find_fully_overlapping_assignments(lines))

    def test_read_assignments(self):
        lines = read_file('test_input')
        self.assertEquals(((2,4),(6,8)) ,core.read_assignments(lines)[0])

    def test_filter_assignment(self):
        self.assertTrue(core.assignments_fully_overlap(((2, 3) , (2, 6))))
        self.assertTrue(core.assignments_fully_overlap(((2, 2) , (1, 4))))
        self.assertFalse(core.assignments_fully_overlap(((2, 3) , (3, 6))))

    def test_filter_partial_assignment(self):
        self.assertTrue(core.assignments_partially_overlap(((2, 3) , (3, 6))))
        self.assertTrue(core.assignments_partially_overlap(((2, 2) , (1, 2))))
        self.assertFalse(core.assignments_partially_overlap(((2, 3) , (4, 6))))

if __name__ == '__main__':
    unittest.main()
