string = input('Введите строку: ').split()

max_word = string[0]

for i in range(len(string)):
    if len(string[i]) > len(max_word):
        max_word = string[i]

print('\nСамое длинное слово: ', max_word)
print('Его длина: ', len(max_word))

# 2й вариант:

# string = input('Введите строку: ').split(' ')
#
# max_len = max([len(i_word) for i_word in string])
#
# print('\nСамое длинное слово: ',
#       [i_word for i_word in string if len(i_word) == max_len])