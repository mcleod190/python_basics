__author__ = 'dima masliukovski'

#Реализовать склонение слова процент для чисел до 20

for i in range(1,20):
    if i == 1:
        ending = ''
    elif 1 < i < 5:
        ending = 'а'
    else:
        ending = 'ов'
    print(i, 'процент' + ending)