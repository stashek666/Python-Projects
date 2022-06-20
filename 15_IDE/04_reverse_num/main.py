def integer_num(a):
    a = int(a)
    n_1 = 0
    while a > 0:
        digit = a % 10
        a = a // 10
        n_1 = (n_1 * 10) + digit
    return n_1


def fractional(a):
    b = round(a % 1, 2)
    c = round(b * 100)

    n_2 = 0

    while c > 0:
        digit = c % 10
        c = c // 10
        n_2 = (n_2 * 10) + digit
    return n_2


N = float(input('Введите первое число: '))
K = float(input('Введите второе число: '))

first_num_1 = integer_num(N)
first_num_2 = fractional(N)

print('Первое число наоборот: ', first_num_1, '.', first_num_2)

sec_num_1 = integer_num(K)
sec_num_2 = fractional(K)
print('Второе число наоборот: ', sec_num_1, '.', sec_num_2)

print('Сумма: ', first_num_1 + sec_num_1, '.', first_num_2 + sec_num_2)

