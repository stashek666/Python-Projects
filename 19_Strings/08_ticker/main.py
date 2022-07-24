str_1 = input('Первая строка: ')
str_2 = input('Вторая строка: ')

count = len(str_1)
result = 0

if str_1 == str_2:
    print('Строки идентичны')
elif len(str_2) != len(str_1):
    print('Первую строку нельзя получить '
          'из второй с помощью циклического сдвига.')
else:
    k = 1
    a = False
    for i in range(len(str_2) - 1):
        str_2 = str_2[-1] + str_2[:-1]
        if str_2 == str_1:
            a = True
            print('Первая строка получается '
                  'из второй со сдвигом', k)
            break
        else:
            k += 1
    if not a:
        print('Первую строку нельзя получить '
              'из второй с помощью циклического сдвига.')
