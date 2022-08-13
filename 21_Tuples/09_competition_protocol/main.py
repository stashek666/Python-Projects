import random
import string

protokol_count = int(input('Сколько записей вносится в протокол? '))
score_dict = {}

for num in range(protokol_count):
    print(num + 1, 'запись:', end=' ')
    random_score = random.randint(50000, 200000)
    random_name = ''.join(random.choice(string.ascii_uppercase)
                          for i in range(random.randint(1, 6)))
    print(random_score, random_name)
    score_dict[random_score] = random_name

score_list = [(score_dict[i_score], i_score)
              for i_score in sorted(score_dict.keys())]
score_list = score_list[::-1]

print('\nИтоги соревнований: ')
for i_winner in range(3):
    print(i_winner + 1, 'место: ', score_list[i_winner])

