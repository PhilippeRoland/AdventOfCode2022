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


def calc_scenic(tree_2d_list, x, y):
    selected_tree_size = tree_2d_list[x][y]
    size = len(tree_2d_list)
    #print(f'scalc_scenic x, y, matrix size: {x}, {y}, {size}')
    if(x == 0 or y == 0 or x == size or y == size):
        return 0
    #print(f'selected tree size : {selected_tree_size}')
    #print(f'neighboring tree sizes : top {tree_2d_list[x-1][y]}, bot {tree_2d_list[x+1][y]}, left {tree_2d_list[x][y-1]}, right {tree_2d_list[x][y+1]}')
    #print(f'unfound bot tree : {tree_2d_list[x+2][y]}')
    #print(f'scanned bot coords {[varx for varx in range(x+1, size)]}')
    #print(f'unfound left tree : {tree_2d_list[x][y-1]}')
    #print(f'scanned left coords {[vary for vary in range(0, y)]}')
    x_coords_block_top = [varx for varx in range(0, x) if tree_2d_list[varx][y] >= selected_tree_size]
    x_coords_block_bot = [varx for varx in range(x+1, size) if tree_2d_list[varx][y] >= selected_tree_size]
    y_coords_block_lef = [vary for vary in range(0, y) if tree_2d_list[x][vary] >= selected_tree_size]
    y_coords_block_rig = [vary for vary in range(y+1, size) if tree_2d_list[x][vary] >= selected_tree_size]
    #print(f'blocking tree indexes: top {x_coords_block_top}, left {y_coords_block_lef}, right {y_coords_block_rig}, bot {x_coords_block_bot}')

    distance_lef = y - (y_coords_block_lef[-1] if len(y_coords_block_lef) > 0 else 0)
    distance_rig = (y_coords_block_rig[0] if len(y_coords_block_rig) > 0 else size-1) - y
    distance_top = x - (x_coords_block_top[-1] if len(x_coords_block_top) > 0 else 0)
    distance_bot = (x_coords_block_bot[0] if len(x_coords_block_bot) > 0 else size-1) - x

    #print(f'distances: top {distance_top}, left {distance_lef}, right {distance_rig}, bot {distance_bot}')
    return distance_lef * distance_rig * distance_top * distance_bot

def solution_2(lines):
    tree_2d_list = parse_trees(lines)
    size = len(tree_2d_list)
    count = 0
    max_scenic = 0
    for i in range(size):
        for j in range(size):
            cur_scenic = calc_scenic(tree_2d_list, i, j)
            if(cur_scenic > max_scenic):
                max_scenic = cur_scenic
    return max_scenic


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
