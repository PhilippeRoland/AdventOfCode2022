import os
from utils import read_file, print_lines


def solution(lines):
    print_lines(lines)
    setup, instructions = parse_input(lines)
    print(setup)

def parse_input(lines):
    #subdivision of lines containing the lines with the stacks formation, minus the column labels at the bottom
    initial_stack_lines = []
    #list of lists
    stacks = []
    stacks_width = 0
    for line in lines:
        if line[-1].isdigit():
            stacks_width = int(line[-1])
            break
        else:
            initial_stack_lines.append(line)

    for i in range(0, stacks_width):
        stacks.append([])

    for line in initial_stack_lines:
        #sample crate line: ^[B]     [Q] [V] [D]     [S]
        #lines have (potentially) the crate letters at index 1, 5, 9, ... up to len-2
        for i in range(1, len(line)-1, 4):
            if not(line[i].isspace()):
                # // is floor division
                crate_index = i//4
                stacks[crate_index].append(line[i])

    return stacks, False






if __name__ == '__main__':
    script_dir = os.path.dirname(__file__)
    lines = read_file(os.path.join(script_dir, 'input'))




    solution = solution(lines)
    print(solution)
    print('----------------------------------------------------------\n'
          '----------------------------------------------------------')