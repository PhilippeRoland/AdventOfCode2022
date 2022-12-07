import os
from utils import read_file, print_lines

def solution(lines):
    print_lines(lines)


if __name__ == '__main__':
    script_dir = os.path.dirname(__file__)
    lines = read_file(os.path.join(script_dir, 'input'))
    solution = solution(lines)
    print(solution)
    print('----------------------------------------------------------\n'
          '----------------------------------------------------------')