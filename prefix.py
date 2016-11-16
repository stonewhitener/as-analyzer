# encoding: utf-8

from argparse import ArgumentParser, FileType


def main(prefix, input_file, output_file):
    path_list = []

    # create the path list
    for line in input_file:
        path = list(map(int, line.split()))
        # insert the ASN at the start of the path
        path.insert(0, prefix)
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
        description='Add the specified ASN to the start of the each path.')
    parser.add_argument('prefix', type=int, metavar='<prefix>', help='the specified ASN')
    parser.add_argument('input_file', type=FileType('r'), metavar='<input_file>',
                        help='input the AS path list from <input_file>')
    parser.add_argument('output_file', type=FileType('w'), metavar='<output_file>',
                        help='output the non-duplicate AS path list into <output_file>')
    args = parser.parse_args()

    main(args.prefix, args.input_file, args.output_file)
