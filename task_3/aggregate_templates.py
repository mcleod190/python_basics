import os
from os.path import abspath, split, join, relpath, basename
from shutil import copy2


def aggregate(path_to_project = './my_project'):
    project_root = join(split(abspath(__file__))[0],path_to_project)
    templates_dir = join(project_root, 'templates')
    #os.mkdir(templates_dir)
    for root, dirs, files in os.walk(project_root):
        if root == project_root: continue
        for file in filter(lambda x: x.endswith('.html'), files):
            dir_path = join(templates_dir, basename(root))
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)
            old_file_path = join(root, file)
            new_file_name = join(templates_dir, basename(root), file)
            copy2(old_file_path, new_file_name)
if __name__ == '__main__':
    aggregate()