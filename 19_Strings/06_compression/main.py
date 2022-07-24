# Вариант с кокнатенацией:
# string = input('Введите строку: ')
#
# count = 1
#
# print('\nЗакодированная строка: ', end='')
# for i_sym in range(len(string)):
#     if i_sym == (len(string)-1):
#         print(string[i_sym] + str(count), end='')
#     else:
#         if string[i_sym] == string[i_sym + 1]:
#             count += 1
#         else:
#             print(string[i_sym] + str(count), end='')
#             count = 1


def compress(s):
    sym_list = list(s[:1])
    s = s[1:]
    parts = [sym_list] if sym_list else []

    for i in sym_list:
        if i in s:
            sym_list.append(i)
        else:
            sym_list = [i]
            parts.append(sym_list)

    return ''.join('{}{}'.format(i_part[0], len(i_part))
                   for i_part in parts)

string = input('Введите строку: ')
result = compress(string)

print('\nЗакодированная строка: ', result)