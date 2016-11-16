# encoding: utf-8

from argparse import ArgumentParser, FileType


def main(input_file, output_file, sort):
    path_list = []
    edge_list = []

    # create the path list
    for line in input_file:
        path = list(map(int, line.split()))
        if len(path) > 0 and path not in path_list:
            path_list.append(path)

    # create the edge list
    for path in path_list:
        # ensure that the path contains 2 and more ASes
        if len(path) >= 2:
            for i in range(len(path) - 1):
                # extract the edge
                edge = path[i:i + 2]
                if edge not in edge_list:
                    # add to the edge list
                    edge_list.append(edge)

    if sort:
        edge_list = sorted(edge_list)

    # write the path list to the specified file
    for edge in edge_list:
        # ensure that the edge contains 2 ASes
        assert len(edge) is 2
        line = str(edge[0]) + ' ' + str(edge[1]) + '\n'
        output_file.write(line)


if __name__ == '__main__':
    parser = ArgumentParser(description='Create the edge list with specified path list.')
    parser.add_argument('input_file', type=FileType('r'), metavar='<input_file>',
                        help='input the AS path list from <input_file>')
    parser.add_argument('output_file', type=FileType('w'), metavar='<output_file>',
                        help='output the edge list into <output_file>')
    parser.add_argument('-s', '--sort', action='store_true', help='sort the path list')
    args = parser.parse_args()

    main(args.input_file, args.output_file, args.sort)
