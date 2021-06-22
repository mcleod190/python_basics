def num_translate(num):
    translations = {'one': 'один', 'two': 'два', 'three': 'три',
    'four': 'четыре', 'five': 'пять', 'six': 'шесть', 'seven': 'семь',
    'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

    return translations.get(num.lower())


def test():
    for num in ['two', 'Three', 'eleven']:
        print(f'{num} переводится: {num_translate(num)}')

test()
