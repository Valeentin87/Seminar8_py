import view
# ------------------- модуль, позволяющий найти и вывести данные сотрудника по имени и фамилии ---------------

def find_name_worker():
    ls = view.worker_dict()
    name = input('введите имя сотрудника')
    surname = input('введите фамилию сотрудника')
    for i in range(len(ls)):
        if ls[i]['first_name'] == name and ls[i]['second_name'] == surname:
            print('мы нашли данные на требуемого сотрудника')
            print(ls[i])
            return ls[i]
        else:
            return print(f'сотрудник {name} {surname} не работает на предприятии')

#find_name_worker()

# --------------------модуль, позволяющий найти сотрудников с заданным диапазоном зарплат--------------------

def find_salary_workers():
    min_salary = int(input('введите минимальную заплату сотрудника в рублях '))
    max_salary = int(input('введите максимальную заплату сотрудника в рублях '))
    ls = view.worker_dict()
    new_ls = []
    count = 0
    for i in range(len(ls)):
        if ls[i]['min_salary'] >= min_salary and ls[i]['max_salary'] <= max_salary:
            count +=1
            new_ls.append(ls[i])

    print(f'На предприятии работает {count} сотрудника с заработной платой от {min_salary} рублей  до  {max_salary} рублей')
    return new_ls

#find_salary_workers()

# --------------------модуль, позволяющий добавить нового сотрудника компании----------------------

def add_new_worker():
    dct = view.worker_dict()
    dct.append({'id_worker': len(dct)+1,
               'second_name': input('введите фамилию нового сотрудника '),
                'first_name': input('введите имя нового сотрудника '),
                'last_name': input('введите отчество нового сотрудника '),
                'post': input('введите должность нового сотрудника '),
                'min_salary': int(input('введите минимальную зарплату ')),
                'max_salary': int(input('введите максимальную зарплату '))})
    return dct[len(dct)-1]


def write_in_data_user(s):
    s_new = list(s.values())
    res_s = ''
    for i in s_new:
        res_s = res_s + str(i)+','
    with open('data_user.txt', 'a', encoding= 'utf-8') as f:
        f.write('\n'+res_s[:-1])

