
def least_divisior(n):
  if n <= 1:
    print ('Ошибка ввода. Число должно быть больше единицы! Пожалуйста повторите ввод.')
  else:
    i = 1
    while i <= n:
        i = i + 1
        if n % i == 0:
            print('Наименьший делитель, отличный от единицы: ', i)
            break

n = int(input('Введите число: '))
least_divisior(n)