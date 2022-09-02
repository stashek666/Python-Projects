def calculating_math_func(data):
    result = 1
    for index in range(1, data + 1):
        result *= index
    result /= data ** 3
    result = result ** 10
    return result


print(calculating_math_func(10))


def calculating_math_func_2(num):

    if num == 1:
        return 1
    factorial = calculating_math_func_2(num - 1)
    return num * factorial


result = (calculating_math_func_2(10) / 10 ** 3) ** 10
print(result)


