import random

original_list = [random.randint(0, 9) for _ in range(10)]
print('Оригинальный список: ', original_list)

print('\n1й способ:')

zip_list = zip(original_list[::2], original_list[1::2])
new_list = [pair for pair in zip_list]

print('Новый список:', new_list)

print('\n2й способ:')

new_list_2 = [(value, original_list[index * 2 + 1])
               for index, value in enumerate(original_list[::2])
               ]

print('Новый список v2:', new_list_2)
