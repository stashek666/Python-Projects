vowels = 'аеёийоуэюя'

text = input('Введите текст: ')

vowels_list = [i_vowels for i_vowels in text
                if i_vowels in vowels]

print('\nСписок гласных букв: ', vowels_list)
print('Длина списка: ', len(vowels_list))
