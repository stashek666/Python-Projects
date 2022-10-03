from random import randint


class House:
    food = 50
    money = 0


class Person:

    def __init__(self, name):
        self.name = name
        self.satiety = 50

    def eat(self):
        self.satiety += 1
        House.food -= 1
        return 'ест, сытость {} еда {}'.format(self.satiety, House.food)

    def work(self):
        self.satiety -= 1
        House.money += 1
        return 'работает, сытость {} деньги {}'.format(self.satiety, House.money)

    def play(self):
        self.satiety -= 1
        return 'играет, сытость {}'.format(self.satiety)

    def repast(self):
        House.food += 1
        House.money -= 1
        return 'идет в магазин, еда {} деньги {}'.format(House.food, House.money)

    def life_person(self, person):
        number_cubes = randint(1, 6)
        if person.satiety < 0:
            print('К сожалению, {} помер с голоду '.format(person.name))
            return False
        if person.satiety < 20 and House.food >= 10:
            text = person.eat()
        elif House.food < 10:
            text = person.repast()
        elif House.money < 50:
            text = person.work()
        elif number_cubes == 1:
            text = person.work()
        elif number_cubes == 2:
            text = person.eat()
        else:
            text = person.play()
        print(person.name, text)
        return True


person_1 = Person('Наруто')
person_2 = Person('Саске')
day = 0

for i in range(365):
    day += 1
    number_cubes = randint(1, 6)
    person = person_1
    person_1.life_person(person)
    if not person_1:
        break
    else:
        person = person_2
        person_2.life_person(person)
        if not person_2:
            break

    print('День {} закончился.'.format(day))


print('\nИтоги года:')
if day == 365 and person_1.satiety > 0:
    print(person_1.name, ' - выжил!')
    print('Уровень здоровья: ', person_1.satiety)
else:
    print('Умер', person_1.name, ' - Умер!')
if day == 365 and person_2.satiety > 0:
    print(person_2.name, ' - выжил!')
    print('Уровень здоровья: ', person_2.satiety)
else:
    print(person_2.name, ' - Умер!')
