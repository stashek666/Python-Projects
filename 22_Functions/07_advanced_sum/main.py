def supple_summ(*args):
    def flatten(a_list):
        result = []
        for e in a_list:
            if isinstance(e, int):
                result.append(e)
            else:
                result.extend(flatten(e))
        return result
    return sum(flatten(args))


lst_1 = [1, 2, [3], [1], 3]
lst_2 = 1, 2, 3, 4, 5
print(lst_1)
print('Ответ: ', supple_summ(lst_1))
print('\n', lst_2)
print('Ответ: ', supple_summ(lst_2))
