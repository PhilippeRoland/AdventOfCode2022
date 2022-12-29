def read_file(file_adress):
    raw_lines = open(file_adress, 'r').readlines()
    # rstrip removes EOLs at the end of the line but doesn't touch whitespace at the beggining
    return list(map(str.rstrip, raw_lines))


def read_file_nostrip(file_adress):
    raw_lines = open(file_adress, 'r').readlines()
    return list(map(str, raw_lines))


def print_lines(lines):
    for line in lines:
        print(line)
