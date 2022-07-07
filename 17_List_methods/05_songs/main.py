violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

N = int(input('Сколько песен выбрать? '))
count = 0

for i_num in range(N):
    print('Название', i_num + 1, 'песни: ', end=' ')
    song = input()
    for index in violator_songs:
        if index[0] == song:
            count += index[1]
print()

print('Общее время звучания песен: ', round(count, 2), 'минут')


