# encoding: utf-8

from argparse import ArgumentParser, FileType


def core_path(input_file, output_file, sort):
    path_list = []
    stub_set = set()
    core_path_list = []

    # create a path list
    for line in input_file:
        path = list(map(int, line.split()))
        if len(path) > 0 and path not in path_list:
            path_list.append(path)

    # create a stub AS list
    for path in path_list:
        stub_candidate = path[-1]
        if stub_candidate not in stub_set:
            # add a stub AS candidate to the stub list
            stub_set.add(stub_candidate)

    for path in path_list:
        if path[:-1] in stub_set:
            # remove the non-stub AS from the stub list
            stub_set.remove(path[:-1])

    # create a core path list without any stubs
    for path in path_list:
        # if the end of the pass is a stub
        if path[-1] in stub_set:
            if len(path[:-1]) > 0 and path[:-1] not in core_path_list:
                core_path_list.append(path[:-1])
        else:
            if path not in core_path_list:
                core_path_list.append(path)

    # sort the core path list if necessary
    if sort:
        core_path_list = sorted(core_path_list)

    # write the path list to the specified file
    for path in core_path_list:
        line = ''
        for num in path:
            line += str(num) + ' '
        output_file.write(line.rstrip() + '\n')


if __name__ == '__main__':
    parser = ArgumentParser(description='Create a core AS path list with the specified AS path list')
    parser.add_argument('input_file', type=FileType('r'), metavar='<input_file>',
                        help='input the BGP route information from <input_file>')
    parser.add_argument('output_file', type=FileType('w'), metavar='<output_file>',
                        help='output the AS path list into <output_file>')
    parser.add_argument('-s', '--sort', action='store_true', help='sort the core path list')
    args = parser.parse_args()

    core_path(args.input_file, args.output_file, args.sort)
