def cipher(text, k):

    alphabet = 'abcdefghijklmnopqrstuvwxyz' \
              'abcdefghijklmnopqrstuvwxyz' \
              'abcdefghijklmnopqrstuvwxyz' \

    result = ''

    for i_sym in text:
        sym_index = alphabet.find(i_sym)
        new_sym_index = sym_index + k
        if i_sym in alphabet:
            result += alphabet[new_sym_index]
        else:
            result += i_sym
    return result


input_file = open(r'C:\python-ds\23_Files\06_paranoia\text.txt')
output_file = open(r'C:\python-ds\23_Files\06_paranoia\cipher_text.txt', 'a')
shift = 0

for i in input_file:
    shift += 1
    res = cipher(i.lower(), shift)
    output_file.write(res.title())

input_file.close()
output_file.close()



