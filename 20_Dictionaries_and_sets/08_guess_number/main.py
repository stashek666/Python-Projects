import random

numbers = int(input('Введите максимальное число: '))
right_num = random.randint(1, numbers)
all_nums = set(range(1, numbers + 1))

while True:
    guess = input('\nНужное число есть среди вот этих чисел: ')
    if guess == 'Помогите!':
        break
    guess = {int(x) for x in guess.split()}
    if right_num in guess:
        print('Ответ Артёма: Да')
        all_nums &= guess
    else:
        print('Ответ Артёма: Нет')
        all_nums -= guess

print('Артём мог загадать следующие числа: ', *all_nums)

#################################################2й вариант:

numbers = int(input('Введите максимальное число: '))
all_nums = set(range(1, numbers + 1))

while True:

    guess = input('\nНужное число есть среди вот этих чисел: ')
    if guess == 'Помогите!':
        break
    guess = {int(x) for x in guess.split()}
    answer = input('Ответ Артёма: ')
    if answer == 'Да':
        all_nums &= guess
    else:
        all_nums -= guess

print('Артём мог загадать следующие числа: ', *all_nums)

