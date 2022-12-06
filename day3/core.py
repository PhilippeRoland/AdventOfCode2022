import os
from utils import read_file, print_lines


def get_total_priority_of_duplicates(lines):
    print_lines(lines)
    compartment_tuples = get_compartments(lines)
    print(compartment_tuples)
    duplicates = list(map(find_dupe, compartment_tuples))
    print(duplicates)
    priorities = list(map(get_priority, duplicates))
    print(priorities)
    return sum(priorities)

def get_compartments(lines):
    return [(line[:len(line)//2], line[len(line)//2:]) for line in lines]

def find_dupe(compartment_tuple):
    for char in compartment_tuple[0]:
        if char in compartment_tuple[1]:
            return char

def get_priority(duplicate):
    if duplicate.isupper():
        return ord(duplicate) - 38
    else:
        return ord(duplicate) - 96

def get_badges_priority(lines):
    print_lines(lines)
    grouped_lines = [lines[i:i+3] for i in range (0,len(lines),3)]
    print_lines(grouped_lines)
    badges = list(map(find_badge, grouped_lines))
    priorities = list(map(get_priority, badges))
    print(priorities)
    return sum(priorities)

def find_badge(group):
    for letter in group[0]:
        if letter in group[1] and letter in group[2]:
            return letter

if __name__ == '__main__':
    script_dir = os.path.dirname(__file__)
    lines = read_file(os.path.join(script_dir, 'input'))
    total_priority_duplicates = get_total_priority_of_duplicates(lines)
    print(total_priority_duplicates)
    print('----------------------------------------------------------\n'
          '----------------------------------------------------------')
    badges_priority = get_badges_priority(lines)
    print(badges_priority)