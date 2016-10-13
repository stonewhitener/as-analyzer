# encoding: utf-8

from argparse import ArgumentParser, FileType


def core_path(in_file, out_file):
    path_list = []
    stub_list = []
    core_path_list = []

    # create a path list
    for line in in_file:
        # eliminate MIRAI's AS
        path = list(map(int, line.split()))[1:]
        if len(path) > 0 and path not in path_list:
            path_list.append(path)

    path_list = sorted(path_list)

    # create a stub AS list
    for path in path_list:
        stub_candidate = path[-1]
        if stub_candidate not in stub_list:
            # add a stub AS candidate
            stub_list.append(stub_candidate)

    for stub_candidate in stub_list[:]:
        for path in path_list:
            if stub_candidate in path[:-1]:
                stub_list.remove(stub_candidate)
                break

    stub_list = sorted(stub_list)

    # create a core path list without any stub AS
    for path in path_list:
        # if the end of the pass is a stub AS
        if path[-1] in stub_list:
            if len(path[:-1]) > 0 and path[:-1] not in core_path_list:
                core_path_list.append(path[:-1])
        else:
            if path not in core_path_list:
                core_path_list.append(path)

    core_path_list = sorted(core_path_list)

    # write to out_file
    for path in core_path_list:
        line = ''
        for num in path:
            line += str(num) + ' '
        out_file.write(line.rstrip() + '\n')


if __name__ == '__main__':
    parser = ArgumentParser(description='Create a core AS path list with the specified AS path list')
    parser.add_argument('in_file', type=FileType('r'))
    parser.add_argument('out_file', type=FileType('w'))
    args = parser.parse_args()

    core_path(args.in_file, args.out_file)
