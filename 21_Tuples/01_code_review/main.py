students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}
#
# def f(dict):
#     lst = []
#     string = ''
#     for i in dict:
#         lst += (dict[i]['interests'])
#         string += dict[i]['surname']
#     cnt = 0
#     for s in string:
#         cnt += 1
#     return lst, cnt
#
#
# pairs = []
# for i in students:
#     pairs += (i, students[i]['age'])
#
#
# my_lst = f(students)[0]
# l = f(students)[1]
# print(my_lst, l)


def students_data(data_dict):

    s_length = ''
    hobby_list = []

    for i_k, i_v in data_dict.items():
        print(i_k, data_dict[i_k]['age'])
        hobby_list.extend(data_dict[i_k]['interests'])
        s_length += data_dict[i_k]['surname']

    return hobby_list, len(s_length)


hobby, surname_length = students_data(students)

print('\n', hobby, surname_length)





