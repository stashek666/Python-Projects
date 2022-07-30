def histogram(string):
    sym_dict = dict()

    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict


def invert(text_dict):
    text_dict_inv = dict()

    for i_letters, i_num in text_dict.items():
        text_dict_inv.setdefault(i_num, []).append(i_letters)
    return text_dict_inv


text = input('Введите текст: ')
hist = histogram(text)

print('Оригинальный словарь частот:')
for i_sym in sorted(hist.keys()):
    print(i_sym, ':', hist[i_sym])

text_dict_invert = invert(hist)

print('\nИнвертированный словарь частот:')

for i_sym in text_dict_invert:
    print('{0} : {1}'.format(i_sym, text_dict_invert[i_sym]))
