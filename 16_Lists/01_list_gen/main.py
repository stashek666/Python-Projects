N = int(input('Введите число: '))
num_list = []

for i in range(1, N + 1):
    if i % 2 != 0:
        num_list.append(i)
print(num_list)