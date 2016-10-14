# encoding: utf-8

from argparse import ArgumentParser, FileType


def as_path(input_file, output_file, legacy, unique, sort, prefix):
    path_list = []
    offset = 50 if legacy else 68

    line_number = 0
    for line in input_file:
        line_number += 1
        # if the line has 'Next hop' column and 'AS path' column
        if len(line) >= offset:
            # extract an 'AS path' column
            column = line[offset:].split()[1:] if legacy else line[offset:].split()
            # if the column is a real 'AS path' column
            if len(column) > 0 and column[-1] in ['I', 'E', '?']:
                # add the prefix AS number if necessary
                path = [] if prefix is None else [prefix]
                # add AS numbers to the path (note that the column's last element is {'I', 'E', '?'})
                for e in column[:-1]:
                    path.append(int(e.strip('{}')))
                # remove duplicates if necessary
                if unique:
                    remove_duplicates(path)
                # add the path to the path list
                # if the path length is larger than 0 and the path is not found in the path list
                if len(path) > 0 and path not in path_list:
                    path_list.append(path)
                    # DEBUG
                    # print(str(line_number) + ': ' + str(path))

    # sort the path list if necessary
    if sort:
        path_list = sorted(path_list)

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
    parser = ArgumentParser(description='Extract the AS paths from the specified BGP route information.')
    parser.add_argument('input_file', type=FileType('r'), metavar='<input_file>',
                        help='input the BGP route information from <input_file>')
    parser.add_argument('output_file', type=FileType('w'), metavar='<output_file>',
                        help='output the AS path list into <output_file>')
    parser.add_argument('-l', '--legacy', action='store_true', help='indicate the legacy format BGP route information')
    parser.add_argument('-u', '--unique', action='store_true', help='remove the duplicates in the path')
    parser.add_argument('-s', '--sort', action='store_true', help='sort the path list')
    parser.add_argument('-p', '--prefix', type=int, metavar='<number>',
                        help='add the specified number to the start of the each path')
    args = parser.parse_args()

    as_path(args.input_file, args.output_file, args.legacy, args.unique, args.sort, args.prefix)
