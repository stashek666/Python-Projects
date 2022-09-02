def move(n, start, finish):

    if n == 1:
        print('\nПереложить диск {0} со стержня {1} на стержень {2}'
              .format(n, start, finish))
    else:
        temp = (6 - start) - finish
        move(n - 1, start, temp)
        print('Переложить диск {0} со стержня {1} на стержень {2}'
              .format(n, start, finish))
        res = (n - 1, temp, finish)

        return print('Переложить диск {0} со стержня {1} на стержень {2}'
                     .format(res[0], res[1], res[2]))


N = int(input('Введите количество дисков: '))
move(N, 1, 3)
