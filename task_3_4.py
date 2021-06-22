# Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия» 
# и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные 
# по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы

test_string = ["Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"]


#helper
def get_lastname_first_letter(name_string):
    last_name = name_string.split()[1]
    return last_name[0]


def get_firstname_first_letter(name_string):
    first_name = name_string.split()[0]
    return first_name[0]


def group_names_by_name_first_letter(*names):
    name_dict = {}
    for name in names:
        firstname_key = get_firstname_first_letter(name)
        if firstname_key in name_dict.keys():
            name_dict[firstname_key].append(name)
        else:
            name_dict[firstname_key] = [name]
    return name_dict


#main function
def thesaurus_adv(*names):
    name_dict = {}
    for name in names:
        last_name_key = get_lastname_first_letter(name)
        names_filtered_by_lastname =  list(filter(lambda x: last_name_key == get_lastname_first_letter(x), names))
        names_grouped_by_first_name = group_names_by_name_first_letter(*names_filtered_by_lastname)
        name_dict[last_name_key] = names_grouped_by_first_name
    return name_dict


print(thesaurus_adv(*test_string))