# Написать декоратор с аргументом-функцией (callback), 
# позволяющий валидировать входные значения функции и выбрасывать исключение ValueError, если что-то не так, например:




def val_checker(condition):
    
    def _val_checker(func):

        def wrapper(*args):
            if not any(map(condition, args)):
                raise ValueError(f'Wrong value: {args}')
            result = func(*args)
            return result
        
        return wrapper
    
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3


def test():
    print(calc_cube(5))
    print(calc_cube(-11))

if __name__ == '__main__':
    test()
