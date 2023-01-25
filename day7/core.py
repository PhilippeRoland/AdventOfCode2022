import os
from utils import read_file, print_lines


def solution(lines):
    print_lines(lines)
    # these inputs always start with $ cd /
    current_dir = Resource("/", 0, None)
    listing_in_progress = False
    for line in lines:
        if line.startswith("$ cd "):
            new_dir = line.replace("$ cd ", "")
            if "/" == new_dir:
                continue
            if ".." == new_dir:
                current_dir = current_dir.parent
            else:
                current_dir = current_dir.find_child(new_dir)

class Resource:
    def __init__(self, name, size, parent):
        # size can be 0, this means it's a dir
        self.name = name
        self.size = size
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def find_child(self, name):
        #this assumes there is such a child, and would fail otherwise
        next(filter(lambda child: child.name == name, self.children))

    def calc_size(self):
        return sum(map(lambda child: child.calc_size(), self.children)) + self.size


if __name__ == '__main__':
    script_dir = os.path.dirname(__file__)
    lines = read_file(os.path.join(script_dir, 'input'))
    solution = solution(lines)
    print(solution)
    print('----------------------------------------------------------\n'
          '----------------------------------------------------------')
