goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}


def count_func(list_item):
    t_quantity = 0
    t_price = 0
    for index in list_item:
        t_price += index['quantity'] * index['price']
        t_quantity += index['quantity']
    return t_quantity, t_price


for item, code in goods.items():
    count, price = count_func(store[code])
    print('{0} - {1} шт, стоимость: {2} руб.'
          .format(item, count, price))
