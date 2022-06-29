N = int(input('Kол-во элементов списка: '))
first_list = []
sec_list = []

for i in range(N):
    first_list.append(int(input('Введите элемент: ')))

print()
shift = int(input('Сдвиг:'))
length = N - shift

for _ in range(length, N):
    sec_list.append(first_list[_])
for _ in range(0, length):
    sec_list.append((first_list[_]))

print('Изначальный список: ', first_list)
print('Сдвинутый список: ', sec_list)