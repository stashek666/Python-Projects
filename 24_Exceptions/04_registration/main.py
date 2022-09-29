def check(line):

    if len(line.split()) < 3:
        raise IndexError('    НЕ присутствуют все три поля')

    name, mail, age = line.split(' ')
    symbols = ('@', '.')
    age = int(age)

    if name.isalpha() is False:
        raise NameError('    Поле имени содержит НЕ только буквы')
    elif age not in range(10, 100):
        raise ValueError('    Поле возраст НЕ является числом от 10 до 99')
    else:
        for char in symbols:
            if char not in mail:
                raise SyntaxError('    Поле емейл НЕ содержит @ и .(точку)')

    return line


with open('registrations.txt', mode='r', encoding='utf-8') as file, \
        open('registrations_bad.log', mode='a', encoding='utf-8') as error, \
        open('registrations_good.log', mode='a', encoding='utf-8') as good:

    for i_elem in file:
        i_elem = i_elem[:-1]
        try:
            string = check(i_elem)
        except IndexError as e:
            error.write(i_elem + str(e) + '\n')
        except NameError as e:
            error.write(i_elem + str(e) + '\n')
        except SyntaxError as e:
            error.write(i_elem + str(e) + '\n')
        except ValueError as e:
            error.write(i_elem + str(e) + '\n')
        else:
            good.write(i_elem + '\n')

print('Готово')


