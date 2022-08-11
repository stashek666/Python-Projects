family_dict = {

    ('Сидоров', 'Никита'): 35,

    ('Сидорова', 'Алина'): 34,

    ('Сидоров', 'Павел'): 10,

    ('Иванов', 'Максим'): 45,

    ('Иванова', 'Мария'): 41

                }


surname = input("Введите фамилию: ").lower()

if surname not in family_dict:
    print('Поиск не дал результатов.')

elif surname[-1] == 'а':

    surname_man = surname[:-1]

    for i_name, i_age in family_dict.items():

        if i_name[0].lower() == surname or i_name[0].lower() == surname_man:
            print(i_name[0], i_name[1], i_age)

else:

    surname_woman = surname + 'а'

    for i_name, i_age in family_dict.items():

        if i_name[0].lower() == surname or i_name[0].lower() == surname_woman:
            print(i_name[0], i_name[1], i_age)
