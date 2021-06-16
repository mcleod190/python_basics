import random

int_list = random.sample(range(100, 1000), 10)
float_list = [x/100 for x in int_list]

#5A: Вывести на экран эти цены через запятую в одну строку, 
# цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).

print('\n5A:')
for price in float_list:
    split_price = str(price).split('.')
    print(f"{split_price[0]} руб {split_price[1].zfill(2)} коп, ", end=' ')


#Вывести цены, отсортированные по возрастанию, новый список не создавать 
# (доказать, что объект списка после сортировки остался тотже)
print('\n\n5B:')
print('initial_list_id:', id(float_list), '\ninitial_list:', float_list)
print('sorted_list_id:', id(float_list))
float_list.sort()
print('sorted_list:', float_list)

#Создать новый список, содержащий те же цены, но отсортированные по убыванию
print('\n\n5C:')

reversed_list = list(sorted(float_list, reverse=True))
print("reversed_list_id:", id(reversed_list))
print("reversed_list:", reversed_list)


#Вывести цены пяти самых дорогих товаров. 
# Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?

print('\n\n5D:')
print('five most expensive items:', reversed_list[:5])