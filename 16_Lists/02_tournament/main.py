names_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']

for i in range(8):
    if i % 2 == 0:
        i += 1
        print(names_list[i], ',', end=' ')