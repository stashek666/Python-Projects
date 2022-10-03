import random


class Ether:
    title = 'Эфир'

    def __add__(self, other):
        if isinstance(other, Air):
            return AirGiant()
        elif isinstance(other, Water):
            return WaterGiant()
        elif isinstance(other, Earth):
            return EarthGiant()
        elif isinstance(other, Fire):
            return FireGiant()
        else:
            raise TypeError


class Fire:
    title = 'Огонь'

    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Earth):
            return Lava()
        else:
            raise TypeError


class Air:
    title = 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            raise TypeError


class Water:
    title = 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            raise TypeError


class Earth:
    title = 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Air):
            return Dust()
        else:
            raise TypeError


class Storm:
    title = 'Шторм'


class Steam:
    title = 'Пар'


class Dirt:
    title = 'Грязь'


class Lightning:
    title = 'Молния'


class Dust:
    title = 'Пыль'


class Lava:
    title = 'Лава'


class WaterGiant:
    title = 'Водный гигант'


class EarthGiant:
    title = 'Земляной гигант'


class FireGiant:
    title = 'Огненный гигант'


class AirGiant:
    title = 'Воздушный гигант'


count = 1

while True:

    water = Water()
    earth = Earth()
    air = Air()
    fire = Fire()
    ether = Ether()
    elements_list = [water, earth, air, fire, ether]
    elem_1 = random.choice(elements_list)
    elem_2 = random.choice(elements_list)

    print('Выбраны элементы: ', elem_1.title, elem_2.title)

    if elem_1 == elem_2:
        count += 1
        print('Попытка номер: ', count)
        elem_1 = random.choice(elements_list)
    else:
        result = elem_1 + elem_2
        print('Смешиваем {} c {} и получаем: {}'.format(
            elem_1.title, elem_2.title, result.title
        ))
        break
