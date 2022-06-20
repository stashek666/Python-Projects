
import math

def coordinate (x, y):
    if x <  0 or y < 0:
        print('Значение должно быть больше нуля! Повторите ввод.')
    else:

      distance = math.sqrt(x ** 2 + y ** 2)

      if distance <= r:
        print('Монетка где-то рядом')
      else:
        print('Монетки в области нет')
      print('Расстояние: ', round(distance, 2))

x = float(input('Введите координату икс: '))
y = float(input('Введите координату игрек: '))
r = int(input('Введите радиус: '))

coordinate (x, y)