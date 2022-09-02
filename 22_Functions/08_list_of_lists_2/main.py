nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]


def flat(user_list, lst=[]):

    for i in user_list:
        if isinstance(i, list):
            flat(i)
        else:
            lst.append(i)
    return lst


print(flat(nice_list))
