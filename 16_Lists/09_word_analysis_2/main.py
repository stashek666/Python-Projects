word = (input('Введите слово: '))

sym_list = list(word)
length = len(sym_list)

length = length - 1
index = 0
no_match = 0

while length - index >= index:
    if sym_list[length - index] == sym_list[index]:
        index += 1
    else:
        no_match = 1
        break

if no_match == 1:
  print()
  print("Слово не является палиндромом")
else:
  print()
  print("Слово является палиндромом")