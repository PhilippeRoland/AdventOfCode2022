import unittest
import core

class Day7Test(unittest.TestCase):
    def test_solution(self):
        self.assertEqual(7, core.solution("mjqjpqmgbljsphdztnvjfqwrcgsmlb"))
        self.assertEqual(5, core.solution("bvwbjplbgvbhsrlpgdmjqwftvncz"))
        self.assertEqual(6, core.solution("nppdvjthqldpwncqszvftbrmjlhg"))
        self.assertEqual(10, core.solution("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"))
        self.assertEqual(11, core.solution("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"))

if __name__ == '__main__':
    unittest.main()
