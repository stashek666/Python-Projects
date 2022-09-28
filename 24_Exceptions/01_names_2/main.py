import logging

logging.basicConfig(filename="errors.log", level=logging.INFO, encoding='utf-8')

count = 0
line = 0

try:

    with open('people.txt', 'r') as input_data:
        for i_name in input_data:
            line += 1
            length = len(i_name)
            if i_name.endswith('\n'):
                length -= 1
            if length < 3:
                raise Exception('Длина {}й строки меньше 3 символов'.format(line))
            count += length

except Exception as e:
    logging.error(str(e))
else:
    print('Программа выполнена без ошибок.')
finally:
    print('Общая сумма символов равна: ', count)
    print(input_data.closed)
