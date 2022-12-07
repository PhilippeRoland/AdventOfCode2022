import os
from utils import read_file, print_lines

def find_fully_overlapping_assignments(lines):
    print_lines(lines)
    assignments = read_assignments(lines)
    overlapping_assignments = list(filter(assignments_fully_overlap, assignments))
    return len(overlapping_assignments)

def read_assignments(lines):
    assignments = []
    for line in lines:
        split_line = line.split(',')
        assignments.append((parse_assignments(split_line[0]), parse_assignments(split_line[1])))
    return assignments
def parse_assignments(assignment_str):
    bounds = assignment_str.split('-')
    return int(bounds[0]), int(bounds[1])

def assignments_fully_overlap(assignment):
    min_1 = min(assignment[0])
    max_1 = max(assignment[0])
    min_2 = min(assignment[1])
    max_2 = max(assignment[1])
    return (min_1 <= min_2 and max_1 >= max_2) or (min_2 <= min_1 and max_2 >= max_1)

def find_partially_overlapping_assignments(lines):
    print_lines(lines)
    assignments = read_assignments(lines)
    overlapping_assignments = list(filter(assignments_partially_overlap, assignments))
    return len(overlapping_assignments)

def assignments_partially_overlap(assignment):
    min_1 = min(assignment[0])
    max_1 = max(assignment[0])
    min_2 = min(assignment[1])
    max_2 = max(assignment[1])
    return (max_1 >= min_2 and min_1 <= min_2) or (max_2 >= min_1 and min_2 <= min_1)

if __name__ == '__main__':
    script_dir = os.path.dirname(__file__)
    lines = read_file(os.path.join(script_dir, 'input'))
    solution = find_fully_overlapping_assignments(lines)
    print(solution)
    print('----------------------------------------------------------\n'
          '----------------------------------------------------------')
    solution2 = find_partially_overlapping_assignments(lines)
    print(solution2)