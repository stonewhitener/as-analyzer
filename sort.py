# encoding: utf-8

from argparse import ArgumentParser, FileType


def sort(input_file, output_file):
    path_list = []

    # create a path list
    for line in input_file:
        path = list(map(int, line.split()))
        if len(path) > 0 and path not in path_list:
            path_list.append(path)

    path_list = sorted(path_list)

    # write the path list to the specified file
    for path in path_list:
        line = ''
        for num in path:
            line += str(num) + ' '
        output_file.write(line.rstrip() + '\n')


if __name__ == '__main__':
    parser = ArgumentParser(description='Sort the specified AS path list.')
    parser.add_argument('input_file', type=FileType('r'), metavar='<input_file>',
                        help='input the AS path list from <input_file>')
    parser.add_argument('output_file', type=FileType('w'), metavar='<output_file>',
                        help='output the sorted AS path list into <output_file>')
    args = parser.parse_args()

    sort(args.input_file, args.output_file)
