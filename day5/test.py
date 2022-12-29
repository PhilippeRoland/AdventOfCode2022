import unittest
import core
from utils import read_file, print_lines


class Day5Test(unittest.TestCase):

    def test_parse_input_stacks(self):
        lines = read_file('test_input')
        print_lines(lines)
        setup, instructions = core.parse_input(lines)
        self.assertEqual(2, len(setup[0]))
        self.assertEqual(3, len(setup[1]))
        self.assertEqual('D', setup[1][0])

    def test_parse_input_instructions(self):
        lines = read_file('test_input')
        print_lines(lines)
        setup, instructions = core.parse_input(lines)
        self.assertEqual(4, len(instructions))
        self.assertEqual('2', instructions[0][0]) #From
        self.assertEqual('1', instructions[0][1]) #To
        self.assertEqual('1', instructions[0][2]) #Quantity

    def test_solution(self):
        lines = read_file('test_input')
        solution, final_setup = core.solution(lines)
        self.assertEqual('CMZ', solution)
        self.assertEqual('N', final_setup[2][1])
        self.assertEqual('D', final_setup[2][2])
        self.assertEqual('P', final_setup[2][3])

if __name__ == '__main__':
    unittest.main()
