from sys import argv
from task_6_4 import smart_strip, process_files

def main(argv):
    program, *args = argv
    if not len(argv) == 4:
        print(f'Not enough arguments. Expected: 3, given: {len(argv) - 1}.')
        exit(1)
    else:
        process_files(*args)
        return 0


if __name__ == '__main__':
    exit(main(argv))


