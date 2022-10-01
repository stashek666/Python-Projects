import random


class Circle:

    pi = 3.14159

    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def circle_info(self):
        print('Координаты x и y: {}, {}\nРадиус: {}\n'.format(
            self.x, self.y, self.r
        ))

    def get_area(self):
        return self.r * self.r * self.pi

    def get_perimeter(self):
        return 2 * self.r * self.pi

    def scale(self, k):
        self.r *= k
        return self.r

    def is_intersect(self, other):
        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2 <= (self.r + other.r) ** 2


circle_1 = Circle(random.randint(0, 10), random.randint(0, 10), random.randint(1, 10))
circle_2 = Circle(random.randint(0, 10), random.randint(0, 10), random.randint(1, 10))
random_increase = random.randint(1, 5)
print('1я окружность: ')
circle_1.circle_info()
print('2я окружность: ')
circle_2.circle_info()

print('Площадь 1й окружности: ', circle_1.get_area())
print('Площадь 2й окружности: ', circle_2.get_area())
print('\nПериметр 1й окружности: ', circle_1.get_perimeter())
print('Периметр 2й окружности: ', circle_2.get_perimeter())
print('\nУвеличение 1й окружности на {}. Радиус:  '.format(
    random_increase), circle_1.scale(random_increase))
print('Увеличение 2й окружности на {}. Радиус: '.format(
    random_increase), circle_2.scale(random_increase))
print('\nПересечение первой окружности со второй: ', circle_1.is_intersect(circle_2))
