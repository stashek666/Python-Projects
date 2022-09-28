import random

errors = [
    'Не повезло',
    'Повезло но не сильно',
    'Вас постигла неудача!'
]

try:

    with open('result.txt', 'a') as result:
        num_sum = 0
        while num_sum < 777:
            num = int(input('Введите число: '))
            num_sum += num
            random_num = random.randint(1, 13)
            if random_num == 13:
                print('Сумма чисел: ', num_sum)
                raise Exception('Выпало число 13')
            else:
                result.write(str(num))
                result.write('\n')

except Exception:
    raise Exception(random.choice(errors))

else:
    print('Все прошло без ошибок.')
finally:
    print(result.closed)


