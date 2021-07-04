from sys import argv
from os import rename, remove

DATABASE = 'bakery.csv'
temp_file = DATABASE + '.tmp'

def main(argv):
    if not len(argv) == 3:
        print(f'Wrong number of arguments. Expected: 2, given: {len(argv) - 1}.')
        exit(1)
    else:
        record_number = int(argv[1])
        value = argv[2]
        with open(DATABASE, 'r', encoding='utf-8') as source, \
            open (temp_file, 'w', encoding='utf-8') as temp:
            for i, line in enumerate(source, start=1):
                if record_number == i:
                    temp.write(value + '\n')
                    continue
                temp.write(line)
        rename(temp_file, DATABASE)
        return 0

if __name__ == '__main__':
    exit(main(argv))