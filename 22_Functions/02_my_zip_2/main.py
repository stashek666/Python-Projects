def my_zip_func(string, some_data, n):

    if n != 0:
        my_zip_func(string, some_data, n - 1)
        tpl = (string[n - 1], some_data[n - 1])
        print(tpl)

    return ''


sym_string = 'abcd'
nums_tpl = (10, 20, 30, 40)
result = my_zip_func(string=sym_string,
                     some_data=nums_tpl,
                     n=min(len(sym_string), len(nums_tpl)))
print(result)
