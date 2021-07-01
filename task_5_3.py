from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А'
]


def match_tutors_w_classes():
    for t, k in zip_longest(tutors, klasses[:len(tutors)]):
        yield t,k


def test():
    gen = match_tutors_w_classes()
    for i in range(len(tutors) + 1):
        print(next(gen))


if __name__ == '__main__':
    test()