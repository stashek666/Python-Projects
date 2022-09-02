def fibonacci_nums(number):
    if number in (1, 2):
        return 1
    return fibonacci_nums(number - 1) + fibonacci_nums(number - 2)


num_pos = int(input('Введите позицию числа в ряде Фибоначчи: '))
print('Число: ', fibonacci_nums(num_pos))
