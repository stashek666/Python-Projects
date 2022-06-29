eff_cells_list = []
N = int(input('Кол-во клеток: '))

for i in range(N):
    print('Эффективность', i + 1, 'клетки: ', end='')
    eff_cells = int(input())
    if eff_cells < i:
        eff_cells_list.append(eff_cells)

print()
print('Неподходящие значения: ', eff_cells_list)