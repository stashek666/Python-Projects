

def summa_n(N):
    num_1 = N // 1
    count = 0
    while num_1 != 0:
        last_num = num_1 % 10
        count += last_num
        num_1 //= 10
    print('Сумма цифр:', count)
    return count

def count_n(N):
    count = 0
    while N != 0:
        N //= 10
        count += 1
    print('Кол-во цифр в числе: ', count)
    return count


N = int(input('Введите число: '))

print()

f_summa = summa_n(N)
f_count = count_n(N)

print('Разность суммы и кол-ва цифр: ', f_summa - f_count)




