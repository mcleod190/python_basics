from sys import argv
from os.path import join
import random
import string



def generate_random_string(n: int):
    chars = string.ascii_lowercase
    return ''.join(random.choice(chars) for _ in range(n))

def create_file(path_to_file: str, content: str):
    with open(path_to_file, 'w') as f:
        f.write(content)


def main(argv):
    if 1 < len(argv) < 3 and int(argv[1]):
        num_files = int(argv[1])
        for i in range(num_files):
            f_name = join('.', 'file_{}.txt'.format(str(i + 1)))
            content = generate_random_string(random.randint(10, 10**5))
            create_file(f_name, content)
        return 0
    else:
        print("You should specify the number of files to generate...")
        return 1

if __name__ == '__main__':
    exit(main(argv))

