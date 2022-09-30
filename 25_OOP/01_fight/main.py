import random


class Warrior:

    def __init__(self, name, health=100):
        self.name = name
        self.health = health

    def hit(self, target):
        if type(self) == type(target):
            target.health -= 20
        else:
            raise TypeError


warriors = [Warrior('Наруто'), Warrior('Саске')]


for _ in range(20):

    i = random.randint(0, 1)
    attacker, victim = warriors[i], warriors[i - 1]
    attacker.hit(victim)

    print('\n{} атаковал {}'.format(attacker.name, victim.name))
    print('У {} осталось здоровья: {}'.format(
        victim.name, victim.health))

    if victim.health <= 0:
        print('\n{} победил!!!'.format(attacker.name))
        break
