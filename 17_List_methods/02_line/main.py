rang_1 = list(range(160,178, 2))
rang_2 = list(range(162, 183, 3))

rang_3 = []
rang_3.extend(rang_1)
rang_3.extend(rang_2)

for i in range(len(rang_3)):
    for i_1 in range(i, len(rang_3)):
        if rang_3[i_1] < rang_3[i]:
            rang_3[i_1], rang_3[i] = rang_3[i], rang_3[i_1]

for i_1 in rang_3:
    for i_2 in range(rang_3.count(i_1) - 1):
        rang_3.remove(i_1)

print(rang_3)