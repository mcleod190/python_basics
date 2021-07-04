from itertools import zip_longest
# (вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ (разумеется, 
# не нужно реально создавать такие большие файлы, это просто задел на будущее проекта). 
# Только теперь не нужно создавать словарь с данными. 
# Вместо этого нужно сохранить объединенные данные в новый файл (users_hobby.txt). 
# Хобби пишем через двоеточие и пробел после ФИО

def smart_strip(line):
    return line.strip() if line else ''


def process_files(users_file, hobbies_file, result_file):
    with open(users_file, 'r', encoding='utf-8') as users_file, \
        open(hobbies_file, 'r', encoding='utf-8') as hobbies_file, \
        open(result_file, 'w', encoding='utf-8') as result_file:
        for u, h in zip_longest(users_file, hobbies_file):
            user = u.strip()
            result_file.write(f'{smart_strip(u)}: {smart_strip(h)}\n')

if __name__ == '__main__':
    process_files('users.csv', 'hobby.csv', 'users_hobby.txt')