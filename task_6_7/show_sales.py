from sys import argv
from math import inf 

DATABASE = 'bakery.csv'

#helper
def print_data(start = 0, end = inf):
    count = 0
    with open(DATABASE, 'r', encoding='utf-8') as f:
        for line in f:
            if count >= start -1: print(line, end='')
            if count >= end -1: break
            count += 1


def main(argv):
    if len(argv) > 3:
        print(f'Wrong number of arguments. Expected: 1 or 2, given: {len(argv) - 1}.')
        exit(1)
    elif len(argv) == 1:
        print_data()
    else:
        sales = list(map(int,argv[1:]))
        print_data(*sales)
        return 0


if __name__ == '__main__':
    exit(main(argv))