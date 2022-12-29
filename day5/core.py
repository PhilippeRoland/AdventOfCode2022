import os
from functools import reduce

from utils import read_file, print_lines



def solution(lines):
    print_lines(lines)
    setup, instructions = parse_input(lines)
    print(setup)
    run_instructions(setup, instructions)
    result_map = map((lambda stack: stack[0] if stack else ''), setup)
    result = reduce((lambda crate1, crate2: crate1+crate2), result_map)
    return result, setup

def solution_2(lines):
    print_lines(lines)
    setup, instructions = parse_input(lines)
    print(setup)
    run_instructions_2(setup, instructions)
    result_map = map((lambda stack: stack[0] if stack else ''), setup)
    result = reduce((lambda crate1, crate2: crate1+crate2), result_map)
    return result, setup

def parse_input(lines):
    #subdivision of lines containing the lines with the stacks formation, minus the column labels at the bottom
    initial_stack_lines = []
    instructions_lines = []
    reading_instructions = False
    #list of lists, orderered left to right and top to bottom
    stacks = []
    stacks_width = 0
    #list of lists, each entry having From, To, Amount in 0, 1, 2 respectively
    instructions = []

    for line in lines:
        if not reading_instructions and line[-1].isdigit():
            stacks_width = int(line[-1])
            reading_instructions = True
        else:
            instructions_lines.append(line) if reading_instructions else initial_stack_lines.append(line)

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

    for line in instructions_lines:
        if line:
            instruction_numbers = list(filter(lambda txt: txt.isnumeric(), line.split(' ')))
            #sample instruction: "move 14 from 2 to 3"
            #turns into [2,3,14]
            instruction = [instruction_numbers[1], instruction_numbers[2], instruction_numbers[0]]
            instructions.append(instruction)

    return stacks, instructions

def run_instructions(setup, instructions):
    for instruction in instructions:
        from_val = int(instruction[0])-1
        to_val = int(instruction[1])-1
        amount = int(instruction[2])
        for i in range(1, amount+1):
            crate = setup[from_val].pop(0)
            setup[to_val].insert(0, crate)

def run_instructions_2(setup, instructions):
    for instruction in instructions:
        from_val = int(instruction[0])-1
        to_val = int(instruction[1])-1
        amount = int(instruction[2])
        for i in range(1, amount+1):
            crate = setup[from_val].pop(0)
            setup[to_val].insert(i-1, crate)

if __name__ == '__main__':
    script_dir = os.path.dirname(__file__)
    lines = read_file(os.path.join(script_dir, 'input'))

    solution, setup = solution(lines)
    print(solution)
    print('----------------------------------------------------------\n'
          '----------------------------------------------------------')
    solution2, setup2 = solution_2(lines)
    print(solution2)