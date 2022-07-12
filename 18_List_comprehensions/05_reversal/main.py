N = input('Введите строку: ')

fst_sym = N[:N.index('h')]
sec_sym = N[N.index('h'):N.rindex('h') + 1]
reverse_sym = N[N.rindex('h') + 1:]
result = fst_sym + sec_sym[::-1] + reverse_sym

print('\nРезультат: ', result)

#
# 2й вариант:
# a = input('Введите строку: ')
# print(a[:a.find("h") + 1] + a[a.rfind("h") - 1:a.find("h"): - 1]
#       + a[a.rfind("h"):])