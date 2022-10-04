import random


class Ether:
    def __str__(self):
        return 'Эфир'

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
    def __str__(self):
        return 'Огонь'

    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Water):
            return Steam()
        elif isinstance(other, Earth):
            return Lava()
        else:
            return FireGiant()


class Air:
    def __str__(self):
        return 'Воздух'

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return AirGiant()


class Water:
    def __str__(self):
        return 'Вода'

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        else:
            return WaterGiant()


class Earth:
    def __str__(self):
        return 'Земля'

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Air):
            return Dust()
        else:
            return EarthGiant()


class Storm:
    def __str__(self):
        return 'Шторм'


class Steam:
    def __str__(self):
        return 'Пар'


class Dirt:
    def __str__(self):
        return 'Грязь'


class Lightning:
    def __str__(self):
        return 'Молния'


class Dust:
    def __str__(self):
        return 'Пыль'


class Lava:
    def __str__(self):
        return 'Лава'


class WaterGiant:
    def __str__(self):
        return 'Водный гигант'


class EarthGiant:
    def __str__(self):
        return 'Земляной гигант'


class FireGiant:
    def __str__(self):
        return 'Огненный гигант'


class AirGiant:
    def __str__(self):
        return 'Воздушный гигант'


count = 1
water = Water()
earth = Earth()
air = Air()
fire = Fire()
ether = Ether()
elements_list = [water, earth, air, fire, ether]
elem_1 = random.choice(elements_list)
elem_2 = random.choice(elements_list)

while True:

    print('Выбраны элементы: ', elem_1, elem_2)

    if elem_1 == elem_2:
        count += 1
        print('Попытка номер: ', count)
        elem_1 = random.choice(elements_list)
    else:
        result = elem_1 + elem_2
        print('Смешиваем {} c {} и получаем: {}'.format(
            elem_1, elem_2, result
        ))
        break
