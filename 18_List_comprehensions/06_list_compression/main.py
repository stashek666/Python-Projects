# Пример:
# Количество чисел в списке: 10
# Список до сжатия: [0, 2, 1, 0, 0, 0, 1, 0, 2, 0]
# Список после сжатия: [2, 1, 1, 2]

import random
N = int(input('Количество чисел в списке: '))

num_list = [random.randint(0, 2) for _ in range(N)]
print('Список до сжатия: ', num_list)

num_list_2 = [i_num for i_num in num_list if i_num]
print('Список после сжатия: ', num_list_2)



