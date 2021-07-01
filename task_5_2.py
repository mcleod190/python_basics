# *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield.


def odd_nums(n):
    return (i for i in range(n+1) if  i % 2)


def test():
    odd_to_15 = odd_nums(15)
    for i in range(10):
        print(i, next(odd_to_15))


if __name__ == '__main__':
    test()
