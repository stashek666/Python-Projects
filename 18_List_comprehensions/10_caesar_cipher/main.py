text = input('Введите сообщение: ').upper()
k = int(input('Введите сдвиг: '))

alfavit = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' \
          'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' \
          'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
result = ''

for i_sym in text:
    sym_index = alfavit.find(i_sym)
    new_sym_index = sym_index + k
    if i_sym in alfavit:
        result += alfavit[new_sym_index]
    else:
        result += i_sym
print('\nрезультат: ', result)
