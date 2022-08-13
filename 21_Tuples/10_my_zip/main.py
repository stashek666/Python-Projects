def shortest_len(string, tpl):

    if not isinstance(string, str):
        str(string)
        return min(len(string), len(tpl))
    elif not isinstance(tpl, tuple):
        tuple(tpl)
        return min(len(string), len(tpl))
    else:
        return min(len(string), len(tpl))

sym_string = 'abcd'
nums_tpl = (10, 20, 30, 40)

pairs = ((sym_string[i_elem], nums_tpl[i_elem])
         for i_elem in range(shortest_len(sym_string, nums_tpl)))
print(pairs)

for i in pairs:
    print(i)

print(zip(sym_string, nums_tpl))