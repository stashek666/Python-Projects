import random


class House:
    food = 50
    money = 100
    cat_food = 30
    dirt = 0
    money_count = 0
    food_count = 0

    def __str__(self):
        return'Состояние дома:\nЕды в холодильнике: {}\n' \
               'Денег в тумбочке: {}\nЕды у кота: {}\n' \
               'Кол-во грязи: {}\n'.format(
            self.food, self.money, self.cat_food, self.dirt
        )


class Resident:

    def __init__(self, name, satiety, happiness):
        self.name = name
        self.satiety = satiety
        self.happiness = happiness

    def eat(self):
        self.satiety += 30
        House.food_count += 30
        House.food -= 30
        print('{} кушает. Сытость: {}'.format(self.name, self.satiety))


class Husband(Resident):
    def __init__(self, name):
        super().__init__(name, satiety=30, happiness=100)
        self.work = 150

    def work_day(self):
        House.money += self.work
        self.satiety -= 10
        House.money_count += self.work
        print('{} идет на работу, деньги {}'.format(
            self.name, House.money))

    def game(self):
        self.happiness += 20
        self.satiety -= 10
        print('{} играет. Счастье: {}'.format(self.name, self.happiness))

    def pretting_cat(self):
        self.happiness += 5
        self.satiety -= 10
        print('{} гладит кота. Счастье: {}'.format(self.name, self.happiness))

    def __str__(self):
        return '{}'.format(self.name)


class Wife(Resident):
    def __init__(self, name):
        super().__init__(name, satiety=30, happiness=100)
        self.fur_coat_count = 0

    def buy_food(self):
        self.satiety -= 10
        House.food += 100
        House.money -= 100
        print('{} идет в магазин, еда {} деньги {}'.format(
            self.name, House.food, House.money
        ))

    def buy_cat_food(self):
        self.satiety -= 10
        House.cat_food += 50
        House.money -= 50
        print('{} покупает еду коту, еда кота {} деньги {}'.format(
            self.name, House.cat_food, House.money
        ))

    def pretting_cat(self):
        self.happiness += 5
        self.satiety -= 10
        print('{} Гладит кота. Счастье: {}'.format(self.name, self.happiness))

    def purchase(self):
        House.money -= 350
        self.happiness += 60
        self.satiety -= 10
        self.fur_coat_count += 1
        print('{} покупает шубу. Деньги {}, счастье: {}'.format(
            self.name, House.money, self.happiness))

    def cleaning(self):
        House.dirt -= 10
        self.satiety -= 10
        print('{} убирает дом, грязь {}'.format(
            self.name, House.dirt
        ))

    def __str__(self):
        return '{}'.format(self.name)


class Cat(Resident):
    def __init__(self, name):
        super().__init__(name, satiety=30, happiness=100)

    def eat(self):
        self.satiety += 20
        House.cat_food -= 10
        print('кот {} ест'.format(self.name))

    def slip(self):
        self.satiety -= 10
        return 'кот {} спит'.format(self.name)

    def shitting(self):
        self.satiety -= 10
        House.dirt += 5
        print('кот {} подрал обои'.format(self.name))

    def __str__(self):
        return '{}'.format(self.name)


house = House()
husband = Husband(name='Саша')
wife = Wife(name='Маша')
cat = Cat(name='Боня')
family_list = [husband, wife, cat]
print('Совместное проживание 2')

for i in range(365):

    print('\nДень {}'.format(i + 1))
    print('\n', house)
    House.dirt += 5

    person = random.choice(family_list)

    if person.satiety <= 0:
        if isinstance(person, Wife):
            print('Этот мир слишком жесток...')
            print('К сожалению, {} умерла от голода!'.format(
                person.name
            ))
        else:
            print('Этот мир слишком жесток...')
            print('К сожалению, {} умер от голода!'.format(
            person.name))
        break

    if person.happiness <= 10 and not isinstance(person, Cat):
        if isinstance(person, Wife):
            print('Этот мир слишком жесток...')
            print('К сожалению, {} умерла от депрессии!'.format(
                person.name
            ))
        else:
            print('Этот мир слишком жесток...')
            print('К сожалению, {} умер от депрессии!'.format(
                person.name
            ))
        break

    if isinstance(person, Cat):
        if random.randint(1, 3) == 1:
            cat.shitting()
        elif random.randint(1, 3) == 2:
            print('Кот спит')
        elif cat.happiness > 100:
            cat.happiness = 100
        elif cat.satiety > 100:
            cat.satiety = 100
        else:
            cat.eat()

    if House.dirt >= 90:
        wife.happiness -= 10
        husband.happiness -= 10

    if isinstance(person, Husband):
        if House.money <= 150:
            husband.work_day()
        elif husband.happiness > 100:
            husband.happiness = 100
        elif husband.satiety > 100:
            husband.satiety = 100
        elif husband.happiness <= 50:
            husband.game()
        elif husband.happiness <= 40:
            husband.pretting_cat()
        elif House.food >= 30:
            husband.eat()

    if isinstance(person, Wife):
        if House.food <= 60 and House.money >= 100:
            wife.buy_food()
        elif wife.happiness > 100:
            wife.happiness = 100
        elif wife.satiety > 100:
            wife.satiety = 100
        elif House.cat_food <= 20:
            wife.buy_cat_food()

        elif House.dirt >= 50:
            wife.cleaning()
        elif wife.happiness <= 50:
            wife.eat()
            wife.pretting_cat()
        elif House.money >= 350:
            wife.purchase()
        else:
            wife.eat()
            wife.happiness += 30

print('\nСостояние семьи: ')

print('{}, здоровье: {}, счастье: {}'.format(
    husband.name, husband.satiety, husband.happiness))
print('{}, здоровье: {}, счастье: {}'.format(
    wife.name, wife.satiety, wife.happiness))
print('{}, здоровье: {}, счастье: {}'.format(
    cat.name, cat.satiety, cat.happiness))

print('\nИтоги года: \nЗаработано денег: {}\nСъедено еды: {}\n'
          'Куплено шуб: {}'.format(
        house.money_count, house.food_count, wife.fur_coat_count))

