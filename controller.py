import view
import  modul


def klick_menu(number):
    if number == 1:
        return modul.find_name_worker()
        # print('\n---------------------------------------------------------------------------------')
        # n = view.menu()
    elif number == 2:
        result = modul.find_salary_workers()
        return print_list(result)
        # print(f'вы добавили нового пользователя \n{g}')
        # print('\n---------------------------------------------------------------------------------')
        # n = view.menu()
    elif number == 3:
        return view.print_all_workers(view.worker_dict())
        # print('\n---------------------------------------------------------------------------------')

    elif number == 4:
        return view.write_txtfile(view.worker_dict())
        # print('\n---------------------------------------------------------------------------------')
        # n = view.menu()
    elif number == 5:
        return modul.add_new_worker()
        # print('\n---------------------------------------------------------------------------------')
        # n = view.menu()

    else:
        return view.data_print('все добавленные сотрудники записаны в базу. Спасибо за работу!')


def print_list(lst):
    for i in lst:
        print(i)