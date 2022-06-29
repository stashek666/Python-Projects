N = int(input('Введите кол-во контейнеров: '))
weight_cont_list = []
count_1 = 1
while N != 0:
    print('Введите вес', count_1, 'контейнера: ', end='')
    weight_cont = int(input())
    if weight_cont <= 0 or weight_cont > 200:
        print()
        print('Ошибка! Все числа должны быть целыми и не должны превышать 200.')
        print('Пожалуйста повторите ввод!')
        print()
        print('Введите вес', count_1, 'Контейнера: ', end='')
        weight_cont = int(input())
    else:
        weight_cont_list.append(weight_cont)
    N -= 1
    count_1 += 1

print()
new_weight_cont = int(input('Введите вес нового контейнера: '))

count = 1
for index in weight_cont_list:
    if new_weight_cont < index:
        count += 1
    else:
        break
print()
print('Номер, куда встанет новый контейнер: ', count)