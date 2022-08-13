def shortest_len(string, tpl):
    return min(len(string), len(tpl))

sym_string = 'abc'
nums_tpl = (10, 20, 30, 40)

pairs = ((sym_string[i_elem], nums_tpl[i_elem])
         for i_elem in range(shortest_len(sym_string, nums_tpl)))
print(pairs)

for i in pairs:
    print(i)

print(zip(sym_string, nums_tpl))
