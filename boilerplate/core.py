import os
from utils import read_file, print_lines

def solution(lines):
    return False

def solution_2(lines):
    return False

if __name__ == '__main__':
    script_dir = os.path.dirname(__file__)
    lines = read_file(os.path.join(script_dir, 'input'))
    print_lines(lines)
    print('----------------------------------------------------------\n'
          '----------------------------------------------------------')
    solution = solution(lines)
    print(solution)
    print('----------------------------------------------------------\n'
          '----------------------------------------------------------')
    solution_2 = solution_2(lines)
    print(solution_2)
