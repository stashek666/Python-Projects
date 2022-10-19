import random


class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __str__(self):
        return ('Информация о человеке:\nИмя: {}\nФамилия: {}\nВозраст: {}'.format(
            self.__name, self.__surname, self.__age))


class Employee(Person):

    def salary(self):
        pass


class Manager(Employee):
    def salary(self):
        return 13000


class Agent(Employee):
    def __init__(self, name, surname, age,
                 volume_of_sales=random.randint(100000, 1000000)):
        super().__init__(name, surname, age)
        self.volume_of_sales = volume_of_sales

    def salary(self):
        return 5000 + round(self.volume_of_sales * 0.05, 2)


class Worker(Employee):
    def __init__(self, name, surname, age,
                 hours=random.randint(100, 160)):
        super().__init__(name, surname, age)
        self.hours = hours

    def salary(self):
        return 100 * self.hours


names = ['Иван', 'Саша', 'Степа', 'Коля', 'Вася', 'Костя']
surnames = ['Иванов', 'Петров', 'Смирнов', 'Белов', 'Крылов', 'Васнецов']

for i in range(3):
    manager = Manager(random.choice(names), random.choice(surnames),
                      random.randint(20, 30))
    agent = Agent(random.choice(names), random.choice(surnames),
                  random.randint(20, 30))
    worker = Worker(random.choice(names), random.choice(surnames),
                    random.randint(20, 30))
    print('Менеджер номер {}\n{}'.format(i + 1, manager))
    print('Зарплата: {}\n'.format(manager.salary()))
    print('Агент номер {}\n{}'.format(i + 1, agent))
    print('Зарплата: {}\n'.format(agent.salary()))
    print('Рабочий номер {}\n{}'.format(i + 1, worker))
    print('Зарплата: {}\n'.format(worker.salary()))
