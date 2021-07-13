import os
import yaml



def create_file(path_to_file):
    with open(path_to_file, 'w') as f: pass


def create_structure(base = '.', d = {}):
    for name, value in d.items():
        curr_path = os.path.join(base, name)
        if type(value) is dict:
            os.mkdir(curr_path)
            create_structure(curr_path, value)
        else:
            create_file(curr_path)


if __name__ == '__main__':
    with open("config.yaml", 'r') as stream:
        struct = yaml.safe_load(stream)
    create_structure(d = struct)
