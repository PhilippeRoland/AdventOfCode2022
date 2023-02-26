import os
import re

from utils import read_file, print_lines

UP_DIR = ".."
ROOT_DIR = "/"

CD_PREFIX = "$ cd "
LS_COMMAND = "$ ls "
DIR_PREFIX = "dir "



def parse_tree(lines):
    # these inputs always start with $ cd /
    # no cd is ever done to a dir that hasn't been seen with ls
    # lines without $ in front are result of an ls and go underneath current dir
    root_dir = Resource(ROOT_DIR, 0, None)
    current_dir = root_dir
    for line in lines:
        if line.startswith(CD_PREFIX):
            new_dir = line.replace(CD_PREFIX, "")
            if ROOT_DIR == new_dir:
                continue
            if UP_DIR == new_dir:
                current_dir = current_dir.parent
            else:
                # ! no error handling !
                current_dir = current_dir.find_child(new_dir)
        elif line.startswith(LS_COMMAND):
            # do nothing; following lines will be listings
            continue
        elif line.startswith(DIR_PREFIX):
            dir_name = line.replace(DIR_PREFIX, "")
            Resource(dir_name, 0, current_dir)
        elif re.match('[0-9]+ .*', line):
            split = line.split(' ')
            size = int(split[0])
            name = split[1]
            # ! could potentially have repeats
            Resource(name, size, current_dir)
    return root_dir

def solution(lines):
    print_lines(lines)
    tree_root = parse_tree(lines)
    solution_size = recursive_solution(tree_root)
    return solution_size

def recursive_solution(node):
    result = 0
    # do not count files, only dirs
    if not node.children:
        return 0
    # only count dirs with size < 100000
    if node.size <= 100000:
        result += node.size
    # sub-dirs also count
    for child in node.children:
        result += recursive_solution(child)
    return result

def solution_2(lines):
    print_lines(lines)
    tree_root = parse_tree(lines)
    space_left = 70000000 - tree_root.size
    min_deletion = 30000000 - space_left
    print(f'Space left: {space_left}')
    dir_sizes = recursive_find_dir_sizes(tree_root)
    dir_sizes.sort()
    return next(filter(lambda size: size >= min_deletion, dir_sizes))

def recursive_find_dir_sizes(node):
    result = []
    # do not count files, only dirs
    if not node.children:
        return result
    result.append(node.size)
    for child in node.children:
        result = result + recursive_find_dir_sizes(child)
    return result


class Resource:
    def __init__(self, name, size, parent):
        # size can be 0, this means it's a dir
        self.name = name
        self.size = size
        self.parent = parent
        self.children = []
        if parent:
            parent.add_child(self)
            # recursively cascade new size upwards
            parent.add_size(self.size)

    def add_child(self, child):
        self.children.append(child)

    def add_size(self, size):
        self.size += size
        if self.parent:
            self.parent.add_size(size)

    def find_child(self, name):
        #this assumes there is such a child, and would fail otherwise
        return next(filter(lambda child: child.name == name, self.children))

    def calc_size(self):
        return sum(map(lambda child: child.calc_size(), self.children)) + self.size


if __name__ == '__main__':
    script_dir = os.path.dirname(__file__)
    lines = read_file(os.path.join(script_dir, 'input'))
    solution = solution(lines)
    print(solution)
    print('----------------------------------------------------------\n'
          '----------------------------------------------------------')
    solution_2 = solution_2(lines)
    print(solution_2)