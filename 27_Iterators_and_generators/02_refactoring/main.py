list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

can_continue = True
for x in list_1:
    for y in list_2:
        result = x * y
        print(x, y, result)
        if result == to_find:
            print('Found!!!')
            can_continue = False
            break
    if not can_continue:
        break

# TODO провести рефакторинг кода
from collections.abc import Iterable


def get_num_gen(lst_1: list, lst_2: list, num: int) -> Iterable[int]:
    for x in lst_1:
        for y in lst_2:
            result = x * y
            print(x, y, result)
            if result == num:
                print('Found!!!')
                yield result
                return


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

res = get_num_gen(lst_1=list_1, lst_2=list_2, num=to_find)

for i in res:
    print('result:', i)
