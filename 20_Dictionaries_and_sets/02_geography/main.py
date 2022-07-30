country_count = int(input('Кол-во стран: '))

country_dict = {}

for i_country in range(country_count):
    print('{} страна: '.format(i_country + 1), end='')
    country_name = input().split()
    for i_value in country_name[1:]:
        country_dict[i_value] = country_name[0]
    print(country_dict)
print()
for i_city in range(3):
    print(i_city + 1, 'город: ', end='')
    city_name = input()
    search_country = country_dict.get(city_name)
    if search_country:
        print('Город {0} расположен в стране {1}.'
              .format(city_name, search_country))

    else:
        print('По городу {} данных нет.'.format(city_name))
