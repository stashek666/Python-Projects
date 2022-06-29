old_v_card_list = []
new_v_card_list = []
N = int(input('Кол-во видеокарт: '))

for i in range(N):
    print(i + 1, 'видеокарта: ', end='')
    v_card = int(input())
    old_v_card_list.append(v_card)

maximum = old_v_card_list[1]
minimum = old_v_card_list[0]

for num in old_v_card_list:

    if num > maximum:
        maximum = num
    if num <= minimum:
        new_v_card_list.append(num)

print()
print('Старый список видеокарт: ', old_v_card_list)
print('Новый список видеокарт: ', new_v_card_list)