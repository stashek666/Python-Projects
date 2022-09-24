import os


def save_files(string):

    way = input('\nКуда хотите сохранить документ? '
                'Введите последовательность папок (через пробел): ')
    file_name = input('\nВведите имя файла: ')

    r_path = way.replace(" ", "/")
    path = 'C:/' + r_path

    if os.path.exists(path):
        real_path = os.path.realpath(os.path.join(path, file_name))
        check_file = os.path.exists(real_path)

        if check_file:

            print('\nФайл с таким именем уже существует!')
            ans_q = input('Вы действительно хотите '
                          'перезаписать файл? (yes/no): ').lower()
            if ans_q == 'yes':
                file = open(real_path, 'w')
                file.write(string)
                print('Файл успешно перезаписан!')
                file.close()
            else:
                print('Файл не перезаписан')
        else:
            file = open(real_path, 'w')
            file.write(string)
            print('Файл успешно сохранён!')
            file.close()
    else:
        print('Такого пути нет')


text = input('Введите строку: ')
save_files(text)

# test_path = 'python-ds 23_Files 05_save'
# test_name = 'text.txt'




