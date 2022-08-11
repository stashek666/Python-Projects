import random


# def sorted_tuple(tuple_):
#
#     list_ = list(tuple_)
#     new_list = []
#
#     for i_num in list_:
#         if isinstance(i_num, int):
#             new_list = [i_num for i_num in sorted(list_)]
#         else:
#             return tuple_
#     if new_list:
#         return tuple(new_list)

def tpl_sort(tpl):
    for element in tpl:
        if not isinstance(element, int):
            return tpl
    return tuple(sorted(tpl))


num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0.1]
number_list = [random.choice(num_list) for _ in range(5)]

tuple_list = tuple(number_list)
print('Изначальный кортеж: ', tuple_list)
print('Результат: ', tpl_sort(tuple_list))

