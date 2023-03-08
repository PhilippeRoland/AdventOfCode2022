import os
import numpy
from utils import read_file, print_lines


def parse_trees(lines):
    tree_2d_list = []
    for line in lines:
        tree_2d_list.append(list(int(c) for c in line))
    return tree_2d_list


def is_visible(tree_2d_list, x, y):
    # assume that input is always a square, and height == width
    size = len(tree_2d_list)
    if x == 0 or y == 0 or x == size - 1 or y == size - 1:
        return True
    else:
        array = numpy.array(tree_2d_list)
        vis_lef = max(array[x, :y]) < tree_2d_list[x][y]
        vis_rig = max(array[x, y+1:]) < tree_2d_list[x][y]
        vis_top = max(array[:x, y]) < tree_2d_list[x][y]
        vis_bot = max(array[x+1:, y]) < tree_2d_list[x][y]
        return vis_top or vis_bot or vis_rig or vis_lef


def solution(lines):
    tree_2d_list = parse_trees(lines)
    size = len(tree_2d_list)
    count = 0
    for i in range(size):
        for j in range(size):
            if is_visible(tree_2d_list, i, j):
                count += 1
    return count



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
