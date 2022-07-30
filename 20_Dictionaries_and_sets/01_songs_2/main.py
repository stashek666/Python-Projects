violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

songs_count = int(input('Сколько песен выбрать? '))

time_count  = 0

for i_song in range(songs_count):

    print('Название {} песни: '.format(i_song + 1), end='')
    name_song = input('')

    if name_song in violator_songs:
        time_count += violator_songs[name_song]
    else:
        print('Такой песни нет в списке!')

print('\nОбщее время звучания песен: ',
      round(time_count, 2), 'минут')
