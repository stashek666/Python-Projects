zen_file = open('zen.txt', 'r')

lst1 = zen_file.read().split('\n')
lst2 = lst1[::-1]

for i_string in lst2:
    print(i_string)

zen_file.close()

