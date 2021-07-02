from time import perf_counter

# Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.


file_path = './logs.log'

def find_max_requests_ip(file_path):
    result_list = dict()
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            ip = line.split()[0]
            if ip in result_list.keys():
                result_list[ip] += 1
            else:
                result_list[ip] = 1
    max_requests = max(result_list.values())
    #print(len(result_list))
    return {k: v for k, v in result_list.items() if v == max_requests}

start = perf_counter()     
print(find_max_requests_ip(file_path))
print(f'spammer found for : {perf_counter() - start}')