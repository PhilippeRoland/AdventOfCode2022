import os
from utils import read_file, print_lines


def max_calories(input_file):
    cals = calories_per_elf(input_file)
    result = max(cals)
    print(result)
    print('-----------------------------')
    return result


def sum_top_three_calories(input_file):
    cals = calories_per_elf(input_file)
    cals.sort()
    result = sum(cals[-3:])
    print(result)
    print('-----------------------------')
    return result

def calories_per_elf(input_file):
    lines = read_file(input_file)
    print_lines(lines)
    print('-----------------------------')
    split_lines = split_cast_lines(lines)
    print('-----------------------------')
    return [sum(elf_line) for elf_line in split_lines]


def split_cast_lines(lines):
    result = []
    tmp_arr = []
    for line in lines:
        if line:
            tmp_arr.append(int(line))
        elif tmp_arr:
            result.append(tmp_arr.copy())
            tmp_arr = []
    result.append(tmp_arr)
    print(result)
    return result


if __name__ == '__main__':
    script_dir = os.path.dirname(__file__)
    max_calories(os.path.join(script_dir, 'input'))
    sum_top_three_calories(os.path.join(script_dir, 'input'))