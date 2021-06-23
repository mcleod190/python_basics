from sys import argv
from utils import currency_rates


def main(argv):
    program, *args = argv
    if not any(map(str.isalpha, args)):
        print('arguments are not a valid currency codes')
        return 1
    for curr in args:
        print(currency_rates(curr))
    return 0


if __name__ == '__main__':
    exit(main(argv))

