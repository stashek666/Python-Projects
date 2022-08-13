def add_contacts(book):

    print('\nВведите имя и фамилию нового контакта: ', end='')
    surname_name = input().title()
    if surname_name in book:
        print('Контакт с таким именем и фамилией уже есть')
    else:
        phone_number = int(input('Номер телефона: '))
        book[surname_name] = phone_number
        print('\nТекущий список контактов: ')
        print(book)


def search_contacts(book):

    search = input('\nВведите фамилию: ').lower()
    result = []
    for index in book:
        if search in index.split()[0].lower():
            result.append(index + ' ' + str(book[index]))
    if not result:
        print('Поиск не дал результатов')
    else:
        for _ in result:
            print(_)


phonebook = {}

while True:
    print('\nВведите команду. \n1 - добавить контакт, '
          '\n2 - найти человека по фамилии, '
          '\n0 - завершить, \nкоманда: ', end='')
    command = int(input())
    if command == 1:
        add_contacts(phonebook)
    elif command == 2:
        search_contacts(phonebook)
    elif command == 0:
        break
