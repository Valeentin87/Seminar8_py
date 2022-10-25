import view
import modul


def klick_menu(number):
    if number == 1:
        return modul.find_name_worker()
    elif number == 2:
        result = modul.find_salary_workers()
        return print_list(result)

    elif number == 3:
        return view.print_all_workers(view.worker_dict())


    elif number == 4:
        return view.write_txtfile(view.worker_dict())

    elif number == 5:
       s = modul.add_new_worker()
       print('новый сотрудник успешно добавлен и записан в файл с базой \'data_user.txt\'')
       return modul.write_in_data_user(s)


    else:
        return view.data_print('все добавленные сотрудники записаны в базу. Спасибо за работу!')


def print_list(lst):
    for i in lst:
        print(i)