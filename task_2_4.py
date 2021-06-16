employees_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 
'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for employee in employees_list:
    name = employee.split()[-1]
    print(f'Привет, {name.capitalize()}!')


