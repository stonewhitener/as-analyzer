# encoding: utf-8

from argparse import ArgumentParser, FileType


def path_list_2013(in_file, out_file, sort):
    path_list = []

    line_number = 0
    for line in in_file:
        line_number += 1
        if 7 <= line_number <= 678321 or 678325 <= line_number <= 697756:
            assert len(line) >= 50
            column = line[50:-3].split()[1:]
            path = []
            for e in column:
                path.append(int(e.strip('{}')))
            if len(path) > 0 and path not in path_list:
                path_list.append(path)
                print(str(line_number) + ': ' + str(path))

    if sort:
        path_list = sorted(path_list)

    for path in path_list:
        line = ''
        for num in path:
            line += str(num) + ' '
        out_file.write(line.rstrip() + '\n')


def path_list_2014(in_file, out_file, sort):
    path_list = []

    skip = False
    line_number = 0
    for line in in_file:
        line_number += 1
        if 7 <= line_number <= 2053995:
            if not skip:
                assert len(line) >= 68
                column = line[68:-3].split()
                path = []
                for e in column:
                    path.append(int(e.strip('{}')))
                if len(path) > 0 and path not in path_list:
                    path_list.append(path)
                    print(str(line_number) + ': ' + str(path))
                skip = True
            else:
                skip = False

    if sort:
        path_list = sorted(path_list)

    for path in path_list:
        line = ''
        for num in path:
            line += str(num) + ' '
        out_file.write(line.rstrip() + '\n')


def path_list_2015(in_file, out_file, sort):
    path_list = []

    skip = False
    line_number = 0
    for line in in_file:
        line_number += 1
        if 7 <= line_number <= 2293782 or 2293788 <= line_number <= 2406485:
            if not skip:
                assert len(line) >= 68
                column = line[68:-3].split()
                path = []
                for e in column:
                    path.append(int(e.strip('{}')))
                if len(path) > 0 and path not in path_list:
                    path_list.append(path)
                    print(str(line_number) + ': ' + str(path))
                skip = True
            else:
                skip = False

    if sort:
        path_list = sorted(path_list)

    for path in path_list:
        line = ''
        for num in path:
            line += str(num) + ' '
        out_file.write(line.rstrip() + '\n')


if __name__ == '__main__':
    parser = ArgumentParser(description='Create a AS path list with the specified AS route information')
    parser.add_argument('in_file', type=FileType('r'))
    parser.add_argument('out_file', type=FileType('w'))
    parser.add_argument('-f', '--format', type=int, choices=[2013, 2014, 2015], required=True)
    parser.add_argument('-s', '--sort', action='store_true')
    args = parser.parse_args()

    if args.format == 2013:
        path_list_2013(args.in_file, args.out_file, args.sort)
    elif args.format == 2014:
        path_list_2014(args.in_file, args.out_file, args.sort)
    elif args.format == 2015:
        path_list_2015(args.in_file, args.out_file, args.sort)
