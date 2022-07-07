rollers_size_list = []
foot_size_list = []

N = int(input('\nКол-во коньков: '))
for i in range(N):
    print('Размер', i + 1, 'пары: ', end = ' ')
    rollers_size = int(input())
    rollers_size_list.append(rollers_size)

K = int(input('\nКол-во людей: '))
for i in range(K):
    print('Размер ноги', i + 1, 'человека: ', end = ' ')
    foot_size = int(input())
    foot_size_list.append(foot_size)

count = 0

for i in foot_size_list:
    for j in range(len(rollers_size_list)):
        if rollers_size_list[j] >= i:
            rollers_size_list.remove(rollers_size_list[j])
            count += 1
            break

print('\nНаибольшее кол-во людей, которые могут взять ролики:', count)
