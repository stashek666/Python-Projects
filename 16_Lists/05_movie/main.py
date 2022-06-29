films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
favorite_films = []

count = 0
while True:
    movie = input('Введите название фильма: ')
    for index in films:
        if index == movie:
            favorite_films.append(movie)
            print('Фильм добавлен в список любимых')
            count += 1
    if count < 1:
        print('Ошибка! Такого фильма нет в списке.')
        break
    count = 0

print()
print('Список любимых фильмов', favorite_films)