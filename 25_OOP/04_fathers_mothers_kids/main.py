import random


class Child:

    calm_states = {0: 'спокоен ', 1: 'плачет '}
    hungry_states = {0: 'сыт ', 1: 'голоден '}

    def __init__(self, child_name, child_age):

        self.name = child_name
        self.age = child_age
        self.calm_state = 0
        self.hungry_state = 0

    def child_info(self):

        print('Имя: {}\nВозраст: {}'.format(
            self.name, self.age
        ))

    def print_state(self):

        print('\nРебенок {} сейчас {}'.format(self.name, Child.calm_states[self.calm_state]))
        print('Ребенок {} сейчас {}\n'.format(self.name, Child.hungry_states[self.hungry_state]))


class Parent:

    def __init__(self, parent_name, parent_age, children_count):

        self.name = parent_name
        self.age = parent_age
        self.children = []
        self.children_count = children_count

    def parent_info(self):

        true_age = True

        while True:
            for i, j in enumerate(self.children):
                if self.age - 16 < i:
                    true_age = False
                    print('Возраст родителя должен быть '
                          'больше на 16 лет возраста ребенка!')
                    print('\nИнформация о детях:')
                    for i_info in self.children:
                        i_info.child_info()
                    self.age = int(input('Введите возраст  {}: '.format(parent_name)))
                else:
                    true_age = True
            if true_age:
                break

        print('\nИнформация о родителе:\nИмя: {}\nВозраст: '
              '{}\nКоличество детей: {}\n'.format(self.name, self.age, self.children_count))

        print('\nИнформация о детях:')
        for i_info in self.children:
            i_info.child_info()

    def soothe_the_child(self, child):

        if child.calm_state == 1:
            print('Родитель {} спешит утешить {}! '.format(self.name, child.name))
            child.calm_state = 0
        else:
            print('Родитель {} рад, что {} спокоен!'.format(self.name, child.name))

    def feed_the_child(self, child):

        if child.calm_state == 1:
            print('Родитель {} спешит накормить {}!'.format(self.name, child.name))
            child.calm_state = 0
        else:
            print('Родитель {} рад, что {} сыт!'.format(self.name, child.name))


children_names_list = ['Sasha', 'Vanya', 'Stepa', 'Veronika']

parent_name = input('Как зовут родителя? ')
parent_age = int(input('Сколько {} лет? '.format(parent_name)))
parent_children_count = random.randint(1, 4)

parent = Parent(parent_name, parent_age, parent_children_count)


for i_count in range(parent_children_count):

    child_name = random.choice(children_names_list)
    child_age = random.randint(1, 10)
    child = Child(child_name, child_age)
    parent.children.append(child)

parent.parent_info()

for i_child in parent.children:

    i_child.calm_state = random.randint(0, 1)
    i_child.hungry_state = random.randint(0, 1)
    i_child.print_state()
    parent.soothe_the_child(i_child)
    parent.feed_the_child(i_child)
