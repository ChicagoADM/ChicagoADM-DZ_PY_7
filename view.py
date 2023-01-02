import os
clear = lambda: os.system('cls')
clear()
def print_data(data):
    if len(data) > 0:
        print("ФАМИЛИЯ".center(15), "ИМЯ".center(15), "ОТЧЕСТВО".center(15),
              "ТЕЛЕФОН".center(15), "АДРЕС".center(20))
        print("-" * 90)
        for item in data:
            print(item[0].ljust(15), item[1].ljust(15), item[2].ljust(15),
                  item[3].ljust(15), item[4].ljust(20))
    else:
        print('В справочнике нет данных!')


def selection_search_menu():
    print('\nИскать по:\n\
        1 - Фамилия;\n\
        2 - Имя;\n\
        3 - Отчество;\n\
        4 - Телефон;\n\
        5 - Адрес;\n\
        0 - выйти из программы')
    choice = input('Выберите параметр, по которому нужно произвести поиск: ')
    return choice


def search_data(data):
    choice = selection_search_menu()
    search = input('Введите данные для поиска: ')
    if choice == '1':
        if len(data) > 0:
            for item in data:
                if search in item:
                    print(f'search {search} item-{item}')
                    return item
    elif choice == '2':
        if len(data) > 0:
                if search in item[1]:
                    return item
    elif choice == '3':
        if len(data) > 0:
            for item in data:
                if search in item[2]:
                    return item
    elif choice == '4':
        if len(data) > 0:
            for item in data:
                if search in item[3]:
                    return item
    elif choice == '5':
        if len(data) > 0:
            for item in data:
                if search in item[4]:
                    return item
    elif choice == '0':
        exit(0)
    else:
        print('Такой команды нет!')
