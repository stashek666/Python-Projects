word_pare = int(input('Введите количество пар слов: '))
word_dict = dict()

for i_word in range(word_pare):
    print('{} пара: '.format(i_word + 1), end='')
    pare = input().title().split(' - ')
    word_dict[pare[0]] = pare[1]
    word_dict[pare[1]] = pare[0]

while True:
    word = input('Введите слово: ').title()
    if word in word_dict:
        print('Синоним: ', word_dict[word])
        break
    else:
        print('Такого слова в словаре нет.')
