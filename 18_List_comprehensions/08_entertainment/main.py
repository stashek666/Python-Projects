import random

N = int(input('Кол-во палок: '))
K = int(input('Кол-во бросков: '))

sticks = ['I' for _ in range(N)]

for K_i in range(K):
    print('\nБросок', K_i + 1, end=' ')
    fst_stick = random.randint(1, N)
    print('Сбиты палки с номера', fst_stick)
    sec_stick = random.randint(fst_stick, N)
    print('по номер ', sec_stick)
    for i_stick in range(fst_stick, sec_stick + 1):
        sticks[i_stick - 1] = '.'

print('\nРезультат: ', ''.join(sticks))