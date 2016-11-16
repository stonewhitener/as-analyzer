# encoding: utf-8

from argparse import ArgumentParser, FileType


def main(input_file):
    path_list = []
    as_set = set()

    # create the path list
    for line in input_file:
        path = list(map(int, line.split()))
        if len(path) > 0:
            path_list.append(path)

    # calc the max path length
    max_path_length = max([len(path) for path in path_list])
    # prepare the path length hist gram
    path_length_hist_gram = [0 for _ in range(max_path_length + 1)]

    for path in path_list:
        # union the as_set
        as_set |= set(path)
        # increment the hist gram list
        path_length_hist_gram[len(path)] += 1

    # print the results
    print('the number of paths: ' + str(len(path_list)))
    print('the number of AS(s): ' + str(len(as_set)))
    print('the hist gram of the path length: ')
    for index, value in enumerate(path_length_hist_gram):
        if index is 0:
            continue
        print(str(index) + ': ' + str(value))


if __name__ == '__main__':
    parser = ArgumentParser(description='Inspect the number of paths, ASes, and show the path length hist gram.')
    parser.add_argument('input_file', type=FileType('r'), metavar='<input_file>',
                        help='input the AS path list from <input_file>')
    args = parser.parse_args()

    main(args.input_file)
