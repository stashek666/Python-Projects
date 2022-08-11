import random


def slicer(tuple_, num):

    if num not in tuple_:
        return ()
    if tuple_.count(num) == 1:
        return tuple_[tuple_.index(num):]
    return tuple_[tuple_.index(num)
                  :tuple_.index(num, tuple_.index(num) + 1) + 1
                  ]


random_list = [random.randint(1, 10) for _ in range(10)]

random_tuple = tuple(random_list)
number = int(input('Введите число: '))

print(random_tuple, number)
print('\n', slicer(random_tuple, number), ', ', number)


