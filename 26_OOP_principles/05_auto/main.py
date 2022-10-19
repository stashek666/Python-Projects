import math


class Auto:
    def __init__(self, x, y, fi):
        self.x = x
        self.y = y
        self.fi = fi

    def move(self, dist):
        self.x = self.x + dist * math.cos(self.fi)
        self.y = self.y + dist * math.sin(self.fi)


class Bus(Auto):

    pay = 0.01
    max_passengers = 60

    def __init__(self, x, y, direction):
        super().__init__(x, y, direction)
        self.passengers = 0
        self.money = 0

    def __str__(self):
        lines = [
            super().__str__(),
            f'В автобусе {self.passengers} пассажиров',
            f'У водителя {round(self.money, 2)} денег',
        ]
        return '\n'.join(lines)

    def move(self, distance):
        self.money += Bus.pay * self.passengers * distance
        super().move(distance)

    def enter(self, passengers):
        if passengers + self.passengers > Bus.max_passengers:
            print('Достигнута максимальная вместимость автобуса')
            print('Уехать смогли только {:d}'.format(
                Bus.max_passengers - self.passengers))
            print('Остались {:d}'.format(
                passengers - (Bus.max_passengers - self.passengers)))
            passengers = Bus.max_passengers - self.passengers
        return passengers

    def exit(self, passengers):
        if passengers > self.passengers:
            print('Вышли все из автобуса')
            passengers = self.passengers

        return passengers

