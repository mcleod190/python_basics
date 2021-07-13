from os import stat, walk
from os.path import join, split, abspath
from collections import defaultdict


def sort_files_by_size(dir_path = None):
    root_path = dir_path if dir_path else split(abspath(__file__))[0]
    print(root_path)
    files_dict = defaultdict(int)
    for root, dirs, files in walk(root_path):
        for file in files:
            file_path = join(root, file)
            files_dict[stat(file_path).st_size] += 1
    return dict(sorted(files_dict.items()))

def group_files_by_size_range(file_dict):
    end_range = len(str(max(file_dict.keys()) * 10))
    grouped_files_dict = defaultdict(int)
    for i in range(1, end_range):
        for size, count in file_dict.items():
            if size < 10**i:
                grouped_files_dict[10**i] +=  count
                file_dict[size] = 0 # это чтобы исключить попадание в бОльший диапазон
    return grouped_files_dict


def main():
    file_dict = sort_files_by_size()
    print(group_files_by_size_range(file_dict))
    return 0

if __name__ == '__main__':
    exit(main())