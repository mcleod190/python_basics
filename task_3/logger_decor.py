#Написать декоратор для логирования типов позиционных аргументов функции, например:


def type_logger(func):

    def wrapper(*args):
        result = func(*args)
        print(f'{func.__name__}({", ".join(map(str,args))}): {", ".join(map(str,(map(type,args))))}')
        return result
    
    return wrapper

@type_logger
def calc_cube(x):
   return x ** 3


def test():
    a = calc_cube(5)
    b = calc_cube(1.3)
    return 0

if __name__ == '__main__':
    exit(test())


