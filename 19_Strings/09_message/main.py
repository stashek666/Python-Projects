message = input('Сообщение: ')

new_message = ''
rev_word = ''
word = ''

for sym in message:
    if sym.isalpha():
        word += sym
    else:
        rev_word = word[::-1]
        new_message += rev_word + sym
        word = ''

print('Новое сообщение: ', new_message)