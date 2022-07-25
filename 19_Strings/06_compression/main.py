def compress(seq):
    start_seq = list(seq[:1])
    end_seq = seq[1:]
    parts = [start_seq] if start_seq else []

    for i_seq in end_seq:
        if i_seq in start_seq:
            start_seq.append(i_seq)
        else:
            start_seq = [i_seq]
            parts.append(start_seq)

    return ''.join('{}{}'.format(part[0], len(part)) for part in parts)

string = input('Введите строку: ')

result = compress(string)
print('\nЗакодированная строка: ', result)

