# encoding: utf-8

from argparse import ArgumentParser, FileType


def sort(input_file, output_file):
    path_list = []

    # create a path list
    for line in input_file:
        path = list(map(int, line.split()))
        # remove duplicates
        path = remove_duplicates(path)
        if len(path) > 0 and path not in path_list:
            path_list.append(path)

    # write the path list to the specified file
    for path in path_list:
        line = ''
        for num in path:
            line += str(num) + ' '
        output_file.write(line.rstrip() + '\n')


def remove_duplicates(duplicated):
    result = []
    for element in duplicated:
        if element not in result:
            result.append(element)
    return result


if __name__ == '__main__':
    parser = ArgumentParser(
        description='Remove the AS number duplicates for the each paths with the specified AS path list.')
    parser.add_argument('input_file', type=FileType('r'), metavar='<input_file>',
                        help='input the AS path list from <input_file>')
    parser.add_argument('output_file', type=FileType('w'), metavar='<output_file>',
                        help='output the non-duplicate AS path list into <output_file>')
    args = parser.parse_args()

    sort(args.input_file, args.output_file)
