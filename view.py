# файл для организации работы с консолью и считыванием данных и записью их в файл-отчёт

def menu():
    print('Добро пожаловать в базу данных сотрудников!')
    print('Введите номер опции,которой хотите воспользоваться')
    print('1. Найти сотрудника в базе по имени и фамилии')
    print('2. Найти сотрудников в заданном диапазоне зарплат')
    print('3. Вывести на экран всех сотрудников компании')
    print('4. Записать в текстовый файл обновленную базу сотрудников')
    print('5. Добавить нового сотрудника')
    print('6. Завершить работу с базой данных')
    number_menu = int(input('пункт меню = '))
    while(number_menu > 6 or number_menu < 1):
        print('введите корректное значение функции меню')
        number_menu = int(input('N = '))
    return number_menu



def worker_dict():
    workers = []
    with open('data_user.txt', 'r', encoding='utf-8') as data:
        for line in data:
            temp = {}
            s = line.split(',')
            temp['id_worker'] = int(s[0])
            temp["second_name"] = s[1]
            temp['first_name'] = s[2]
            temp['last_name'] = s[3]
            temp['post'] = s[4]
            temp['min_salary'] = int(s[5])
            temp['max_salary'] = int(s[6])
            workers.append(temp)
    return workers

#print(worker_dict())


# -----------метод, выводящий в консоль то, что необходимо напечатать---------------------
def data_print(data):
    return print(data)

# ------------метод, выводящий в консоль  имеющиеся данные по сотрудникам-----------------

def print_all_workers(list):
    print('Ниже представлены данные по всем имеющимся сотрудникам предприятия')
    for i in range(len(list)):
        print(list[i])

    print('\n ---------данные по сотрудникам записаны в файл \'all.workers.txt\' ------------------------')

#print_all_workers(worker_dict())


# ----------------метод,позволяющий записать в txt файл данные по всем сотрудникам-------------------
def write_txtfile(list):
    with open('all_workers.txt', 'a', encoding='utf-8') as f:
        for line in range(len(list)):
            s = str(list[line])
            f.writelines('\n' + s)
    print('\n ---------данные по сотрудникам записаны в файл \'all.workers.txt\' ------------------------')




