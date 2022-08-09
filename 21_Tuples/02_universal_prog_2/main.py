import random


def is_prime(number):
    if number == 2 or number == 3:
        return True
    elif number % 2 == 0 or number < 2:
        return False
    for i_num in range(3, int(number ** 0.5) + 1, 2):
        if number % i_num == 0:
            return False
    return True


def if_is_prime(data):

    return [data_value
            for data_key, data_value in enumerate(data)
            if is_prime(data_key)
            ]


string_str = 'О Дивный Новый мир!'
string_list = [100, 200, 300, 'буква', 0, 2, 'а']
string_dict = {'1': 10, '2': 20, '3': 30, '4': 'бук', '5': 22}
string_tuple = (1, 2, 'abc', 3, 4, 5)

choice_list = [string_list, string_dict, string_str,
               string_tuple
               ]

choice = random.choice(choice_list)

if isinstance(choice, str):
    print('Допустим, есть такая строка:', choice)
    print('Результат: ', if_is_prime(choice))

elif isinstance(choice, list):
    print('Допустим, есть такой список:', choice)
    print('Результат: ', if_is_prime(choice))

elif isinstance(choice, dict):
    print('Допустим, есть такой словарь:', choice)
    new_dict = {i: choice[i]
                for i in if_is_prime(choice)
                }
    print(new_dict)

elif isinstance(choice, tuple):
    print('Допустим, есть такой кортеж:', choice)
    print('Результат: ', if_is_prime(choice))


