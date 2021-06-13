__author__ = 'dima masliukovski'


#Создать список, состоящий из кубов нечётных чисел от 1 до 1000

cubes = []
for number in range(1000):
    if number % 2:
        cubes.append(number**3)

# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7

sum_of_divisibles = 0

for number in cubes:
    sum_of_digits = 0
    copy_of_number = number
    while copy_of_number > 0:
        sum_of_digits = sum_of_digits + copy_of_number % 10
        copy_of_number = copy_of_number // 10
    if not sum_of_digits % 7:
        sum_of_divisibles += number
print('2a:', sum_of_divisibles)

#К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, 
# сумма цифр которых делится нацело на 7

sum_of_divisibles = 0

for number in cubes:
    sum_of_digits = 0
    copy_of_number = number + 17
    while copy_of_number > 0:
        sum_of_digits = sum_of_digits + copy_of_number % 10
        copy_of_number = copy_of_number // 10
    if not sum_of_digits % 7:
        sum_of_divisibles += number
print('2b:', sum_of_divisibles)