
N = int(input('Введите длину списка: '))

N_list = [1 if i_num % 2 == 0 else i_num % 5
          for i_num in range(N)]

print('\nРезультат: ', N_list)
