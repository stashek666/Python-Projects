first_list = []
second_list = []

for i in range(3):
    print('Введите', i + 1, '-е число для первого списка: ', end = ' ')
    number_first_list = int(input())
    first_list.append(number_first_list)

print()
for i in range(7):
    print('Введите', i + 1, '-е число для второго списка: ', end=' ')
    number_second_list = int(input())
    second_list.append(number_second_list)

print('Первый список:', first_list, '\nВторой список:', second_list)

first_list.extend(second_list)

for number in first_list:
    for quantity_remove in range(first_list.count(number) - 1):
        first_list.remove(number)

print('\nНовый первый список с уникальными элементами: ', first_list)

#2й вариант:
#
# first_list = []
# second_list = []
#
# for i in range(3):
#     print('Введите', i + 1, '-е число для первого списка: ', end = ' ')
#     number_first_list = int(input())
#     first_list.append(number_first_list)
#
# for i in range(7):
#     print('Введите', i + 1, '-е число для второго списка: ', end=' ')
#     number_second_list = int(input())
#     second_list.append(number_second_list)
#
# print('Первый список:', first_list, '\nВторой список:', second_list)
#
# first_list.extend(second_list)
#
#
# for _ in first_list:
#     while first_list.count(_) >= 2:
#         first_list.remove(_)
#
# print('\nНовый первый список с уникальными элементами: ', first_list)