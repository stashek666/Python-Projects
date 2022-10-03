class Potato:

    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Картошка {} сейчас {}'.format(
            self.index, Potato.states[self.state]))
        if self.state == 3:
            Gardener.potato_count.append(self.index)


class PotatoGarden:

    cnt = 1

    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Обход {}'.format(self.cnt))
        print('Картошка прорастает!\n')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        if not all(i_potato.is_ripe() for i_potato in self.potatoes):
            print('\nКартошка еще не созрела!\n')
            self.cnt += 1

        else:
            print('Вся картошка созрела. Можем собирать!\n')
            print('Количество обходов: {}'.format(self.cnt))


class Gardener:

    potato_count = []

    def __init__(self, name, garden):
        self.name = name
        self.garden = garden

    def take_care_of_the_garden(self):
        print('Садовник {} ухаживает за грядкой {}\n'.format(
            self.name, self.garden))

    def harvest_garden(self):
        print('\nСадовник {} начал собирать урожай!\nСобрано картошки: {}'.format(
            self.name, len(self.potato_count)))


my_garden = PotatoGarden(5)
gardener = Gardener('Vanya', 'Картошка')

for i in range(5):
    potato = Potato(i)
    potato.print_state()

for _ in range(3):

    gardener.take_care_of_the_garden()
    my_garden.grow_all()
    my_garden.are_all_ripe()

gardener.harvest_garden()
