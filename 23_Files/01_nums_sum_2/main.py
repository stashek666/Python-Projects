input_data_file = open('numbers.txt', 'r', encoding='utf-8')

data_list = input_data_file.read().split()
summa = 0

for num in data_list:
    summa += int(num)
input_data_file.close()

output_data_file = open('answer.txt', 'w', encoding='utf-8')
output_data_file.write(str(summa))
output_data_file.close()
