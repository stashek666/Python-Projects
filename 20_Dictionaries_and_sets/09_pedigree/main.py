def height(human):
    if human not in p_tree:
        return 0
    else:
        return 1 + height(p_tree[human])


p_tree = dict()
n = int(input('Введите количество человек: '))
for i in range(n - 1):
    print(i + 1, 'пара: ', end='')
    pare = input().split()
    child = pare[0]
    parent = pare[1]
    p_tree[child] = parent

heights = dict()

for man in set(p_tree.keys()).union(set(p_tree.values())):
    heights[man] = height(man)

print('\n“Высота” каждого члена семьи: ')
for key, value in sorted(heights.items()):
    print(key, value)
