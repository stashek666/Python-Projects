string = open("text.txt", "r").read().lower()

sym_dict = {}
count = 0

for i_sym in string:

   if ord('a') <= ord(i_sym) <= ord('z'):
       find_sym = sym_dict.get(i_sym, 0)
       sym_dict[i_sym] = find_sym + 1
       count += 1

frequency_list = [(i_key, "{:5.3f}".format(sym_dict[i_key]/count))
                  for i_key in sym_dict.keys()]

frequency_list.sort(key=lambda x: x[0])
frequency_list.sort(key=lambda x: x[1], reverse=True)

result = "\n".join([i_elem[0] + " " + i_elem[1]
                    for i_elem in frequency_list])

output_data = open("output.txt", "w")
output_data.write(result)

output_data.close()
