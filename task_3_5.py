import random as rd
# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, 
# взятых из трёх списков (по одному из каждого)



NOUNS = ["автомобиль", "лес", "огонь", "город", "дом"]
ADVERBS = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
ADJECTIVES = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


#helper functions
def generate_jokes(n):
    n_nouns, n_adverbs, n_adjectives = list(rd.choices(NOUNS, k = n)), rd.choices(ADVERBS, k = n), rd.choices(ADJECTIVES, k = n)
    jokes = zip(n_nouns, n_adverbs, n_adjectives)
    return list(map(' '.join, jokes))


def generate_unique_jokes(n):
    n_nouns, n_adverbs, n_adjectives = list(rd.sample(NOUNS, n)), rd.sample(ADVERBS, n), rd.sample(ADJECTIVES, n)
    jokes = zip(n_nouns, n_adverbs, n_adjectives)
    return list(map(' '.join, jokes))

#main function
def get_jokes(n = 1, allow_repetition = True):
    if allow_repetition:
        jokes = generate_jokes(n)
    else:
        jokes = generate_unique_jokes(n)
    return jokes


#for testing:
def test():
    numbers = list(range(2,len(NOUNS)))
    flags = [True, False]
    n, allow_repetition = rd.choice(numbers), rd.choice(flags)
    print(f"Getting jokes with n = {n} and allow_repetition = {allow_repetition}\n")
    print(get_jokes(n, allow_repetition))

test()



        