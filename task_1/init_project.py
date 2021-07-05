from os import makedirs
from sys import argv
import os.path


structure = {
    'subdirectories': [
        'settings',
        'mainapp',
        'adminapp',
        'authapp'
    ]
}

def create_structure(init_path = '.', project_name = 'my_project'):
    for subdir in structure['subdirectories']:
        makedirs(os.path.join(init_path, project_name, subdir))
    print('Project is ready!')

def main(argv):
    if len(argv) > 3:
        print(f'Wrong number of arguments. Expected: 2, given: {len(argv) - 1}.')
        return 1
    else:
        args = argv[1:]
        create_structure(*args)
    return 0


if __name__ == '__main__':
    exit(main(argv))