from collections.abc import Iterable


def hofstadter_seq(start: list) -> Iterable[int]:
    if start != [1, 1]:
        print('End')
        return
    seq = start[:]
    while 1:
        q = seq[-seq[-1]] + seq[-seq[-2]]
        seq.append(q)
        yield q


N = int(input('Сколько чисел в последовательности: '))
counter = 1
result = hofstadter_seq(start=[1, 1])

print('Результат:')
for i in result:
    if counter > N:
        break
    print(i, end=' ')
    counter += 1
