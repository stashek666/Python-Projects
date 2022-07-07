guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

text = ''

while text != 'Пора спать':
    print('Сейчас на вечеринке', len(guests), 'человек: ', guests)
    text = input('Гость пришел или ушел? ')
    if text == 'пришел':
        name = input('Имя гостя: ')
        if len(guests) < 6:
            print('Привет, ', name, '!')
            guests.append(name)
        else:
            print('Прости, ', name, ',но мест нет.')
    elif text == 'ушел':
        name = input('Имя гостя: ')
        print('Пока, ', name, '!')
        guests.remove(name)
    print()

print()
print('Вечеринка закончилась, все легли спать.')