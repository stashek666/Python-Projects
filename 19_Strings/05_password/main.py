def count_digit(string):
    count = 0
    for i in string:
        if i.isdigit():
            count += 1
    return count


while True:
    password = input('Придумайте пароль: ')
    # for i in password:
    #     if i.isdigit():
    #         count += 1
    if len(password) < 8:
        print('Пароль ненадёжный! Должно быть не менее 8 символов. '
              'Попробуйте ещё раз.')
    elif password.islower():
        print('Пароль ненадёжный! Должна быть хотя '
              'бы одна буква из верхнего регистра. Попробуйте ещё раз.')
    elif count_digit(password) < 3:
        print('Пароль ненадёжный! Должно быть минимум 3 цифры.'
              'Попробуйте ещё раз.')
    else:
       print('Это надёжный пароль!')
       break
