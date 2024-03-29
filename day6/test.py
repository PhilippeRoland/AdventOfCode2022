import unittest
import core

class Day7Test(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(7, core.solution("mjqjpqmgbljsphdztnvjfqwrcgsmlb"))
        self.assertEqual(5, core.solution("bvwbjplbgvbhsrlpgdmjqwftvncz"))
        self.assertEqual(6, core.solution("nppdvjthqldpwncqszvftbrmjlhg"))
        self.assertEqual(10, core.solution("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"))
        self.assertEqual(11, core.solution("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"))

    def test_solution_2(self):
        self.assertEqual(19, core.solution_2("mjqjpqmgbljsphdztnvjfqwrcgsmlb"))
        self.assertEqual(23, core.solution_2("bvwbjplbgvbhsrlpgdmjqwftvncz"))
        self.assertEqual(23, core.solution_2("nppdvjthqldpwncqszvftbrmjlhg"))
        self.assertEqual(29, core.solution_2("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"))
        self.assertEqual(26, core.solution_2("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"))

if __name__ == '__main__':
    unittest.main()
