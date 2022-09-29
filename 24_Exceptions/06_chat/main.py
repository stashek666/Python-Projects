import time

user_name = input('Введите имя: ')

while True:

    print('Введите 1, чтобы увидеть историю сообщений,'
          'введите 2, чтобы написать сообщение.')
    command = input('Введите команду(1/2): ')
    if command == '1':
        try:
            with open('chat.txt', 'r', encoding='utf-8') as file:
                history_messages = file.readlines()
                print(''.join(history_messages))
        except FileNotFoundError:
            print('История сообщений пуста!\n')
    elif command == '2':
        message = input('Введите сообщение: ')
        with open('chat.txt', 'a', encoding='utf-8') as file:
            file.write('{name}: {text}\n'.format(name=user_name, text=message))
    else:
        print('Неизвестная команда\n')
