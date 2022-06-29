def sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True

N = int(input('Сколько чисел будем вводить?: '))
nums_list = []

for i in range(N):
    print('Введите', i + 1, 'е', 'число: ', end='')
    num = int(input())
    nums_list.append(num)

sort(nums_list)
print()
print('Отсортированный список: ', nums_list)