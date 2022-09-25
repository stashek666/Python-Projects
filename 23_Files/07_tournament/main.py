first_tour_data = open(r'C:\python-ds\23_Files\07_tournament\first_tour.txt')

tour_score = int(first_tour_data.readline())
new_list = []

for elem in first_tour_data:
    result = elem.split()
    if int(result[-1]) > tour_score:
        new_list.append(result)

first_tour_data.close()

new_list.sort(key=lambda a: int(a[-1]))
new_list.reverse()

count = str(len(new_list))

out_lst = []
n = 1

for i in new_list:
    name_sim = str(i[1][0]) + '.'
    s_win = str(n) + ') ' + name_sim + ' ' + i[0] + ' ' + i[2]
    out_lst.append(s_win)
    n += 1

with open("second_tour.txt", "w", encoding='utf-8') as f_out:
    f_out.write(count + '\n')
    s = '\n'.join(out_lst)
    f_out.write(s)
