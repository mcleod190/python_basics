# Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, 
# в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы



test_names = ["Иван", "Мария", "Петр", "Илья"]
def thesaurus(*names):
    name_dict = {}
    for name in names:
        k = name[0]
        if k in name_dict.keys():
            name_dict[k].append(name)
        else:
            name_dict[k] = [name]
    return name_dict


print(thesaurus(*test_names))