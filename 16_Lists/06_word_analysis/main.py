word = input('Введите слово: ')
sym_list = list(word)
universal_sym = 0

for sym_1 in sym_list:
    same_sym = 0
    for sym_2 in sym_list:
        if sym_2 == sym_1:
            same_sym += 1
    if same_sym == 1:
         universal_sym += 1

print('Кол-во уникальных букв', universal_sym)