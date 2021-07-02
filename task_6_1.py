# Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt


file_path = './logs.log'



def parse_logfile(file_path):
    result_list = []

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line_splitted = line.split()
            result_list.append((line_splitted[0], line_splitted[5].replace('"',''), line_splitted[6]))
    return result_list

if __name__ == '__main__':
    print(parse_logfile(file_path))