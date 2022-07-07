N = int(input('Кол-во друзей: '))
K = int(input('Кол-во расписок: '))

friends = []
for friend in range(1, N + 1):
    friends.append(list([friend, 0]))

for receipts in range(K):
    print('\n', receipts + 1, 'расписка')
    print('Кому: ', end=' ')
    debtor = int(input())
    print('От кого:: ', end=' ')
    creditor = int(input())
    print('Сколько: ', end=' ')
    credit = int(input())
    friends[debtor - 1][1] -= credit
    friends[creditor - 1][1] += credit

print('\nБаланс друзей: ')
for index in range(len(friends)):
    print(friends[index][0], ':', friends[index][1])