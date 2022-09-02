def num_range(num, i_num=1):

    print(i_num, end=' ')
    if i_num != num:
        num_range(num, i_num + 1)


number = int(input('Введите число: '))
num_range(number)
