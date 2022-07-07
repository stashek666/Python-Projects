N = int(input('Кол-во человек: '))
K = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', K, 'человек.')
mens_list = list(range(1, N + 1))
out = 0

for _ in range(N - 1):
    print('\nТекущий круг людей', mens_list)
    start_count = out % len(mens_list)
    out = (start_count + K - 1) % len(mens_list)
    print('Начало счёта с номера', mens_list[start_count])
    print('Выбывает человек под номером', mens_list[out])
    mens_list.remove(mens_list[out])

print('\nОстался человек под номером', mens_list)
