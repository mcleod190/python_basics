from sys import argv

def main(argv):
    if not len(argv) == 2:
        print(f'Wrong number of arguments. Expected: 1, given: {len(argv) - 1}.')
        exit(1)
    else:
        program, sale = argv
        #print(sale)
        with open('bakery.csv', 'a+', encoding='utf-8') as f:
            f.writelines(sale + '\n')
        return 0


if __name__ == '__main__':
    exit(main(argv))