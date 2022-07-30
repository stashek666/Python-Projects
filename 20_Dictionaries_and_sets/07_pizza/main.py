def get_pizza_list(dct, key, num):
    dct[key] = dct.setdefault(key, 0) + int(num)
    return dct


orders_dict = dict()

for i_order in range(int(input('Введите кол-во заказов: '))):
    print(i_order + 1, 'заказ: ', end='')
    order = input().split()

    name = order[0]
    pizza = order[1]
    count = order[2]

    orders_dict[name] = get_pizza_list(orders_dict.get(name, {}),
                                       pizza, count)


print()
for name in sorted(orders_dict):
    print(f'{name}:')
    for pizza, count in sorted(orders_dict.get(name).items()):
        print('{0}: {1}'.format(pizza, count))
    print()
