num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))

print()
print('Года от', num1, 'до', num2, 'с тремя одинаковыми цифрами:')

for num in range(num1, num2 + 1):

    count1 = num // 1000
    count2 = (num // 100) % 10
    count3 = (num % 100) // 10
    count4 = num % 10

    if count1 == count2 == count3:
        print(num)
    elif count2 == count3 == count4:
        print(num)
    elif count1 == count3 == count4:
        print(num)