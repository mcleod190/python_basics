

initial_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

print('initial array:', initial_list, '\n')

element_index = 0

#мы будет менять начальный список, поэтому каждый раз заново вычисляем его длину
while element_index < len(initial_list):
    if initial_list[element_index][-1].isnumeric():
        zero_prefixed_number = initial_list[element_index].zfill(len(initial_list[element_index]) + 1)
        initial_list[element_index] = zero_prefixed_number
        initial_list.insert(element_index, '"')
        element_index += 2
        initial_list.insert(element_index, '"')
    else:
        element_index += 1

print('modified array:', initial_list, '\n')

string_from_array = ''
quotes_counter = 0


#дичь конечно, но я не придумал как еще избавить от пробелов между кавычкой и цифрой
for el in initial_list:
    if el == '"':
        quotes_counter += 1
        if quotes_counter % 2:
            string_from_array += el
        else:
            string_from_array += (el + ' ')
    elif el[-1].isnumeric():
        string_from_array += el
    else:
        string_from_array += (el + ' ')

print('string_from array:', string_from_array, '\n')
