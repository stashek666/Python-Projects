from collections.abc import Iterable

class SquareIter:
    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.counter = 0
        self.first_elem = 0

    def __iter__(self):
        self.first_elem = 0
        self.counter = 0
        return self

    def __next__(self) -> int:
        self.counter += 1
        if self.counter > self.limit:
            raise StopIteration
        self.first_elem += 1
        return self.first_elem * self.first_elem


def square_gen(n: int) -> Iterable[int]:
    for i_elem in range(1, n + 1):
        yield i_elem ** 2


N = int(input('Сколько чисел в последовательности: '))

print('\n1. Класс - итератор:')
res = SquareIter(limit=N)
for i in res:
    print(i, end=' ')
print()

print('\n2. Функция - генератор: ')
res = square_gen(n=N)

for elem in res:
    print(elem, end=' ')
print()

print('\n3. Генераторное выражение: ')
res = (elem ** 2 for elem in range(1, N + 1))
for elem in res:
    print(elem, end=' ')
