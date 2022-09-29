with open('calc.txt', 'r') as file:

    print('Содержимое файла calc.txt')
    for i in file:
        print(i)

result = []

with open('calc.txt', 'r') as file:

    print('\nСодержимое консоли:')
    for line in file.readlines():
        try:
            result.append(eval(line))
        except SyntaxError:

            if input('Обнаружена ошибка в строке:' +
                     line + 'Хотите исправить?(yes/no): ') == 'yes':
                line = input('Введите исправленную строку: ')
                result.append(eval(line))

print('\nСумма результатов:', sum(result))
