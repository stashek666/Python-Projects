while True:
    ip_adress = input('Введите IP: ').split('.')
    #split_ip = ip.split('.')

    count_1 = 0
    count_2 = 0

    if len(ip_adress) < 4:
        print('Адрес - это четыре числа, разделенные точками')
    else:
        for i in range(len(ip_adress)):
            if ip_adress[i].isdigit():
                count_2 += 1
                if int(ip_adress[i]) > 255:
                    count_1 += 1
                    print(f'{ip_adress[i]} превышает 255')
            else:
                print(f'{ip_adress[i]}- не целое число')

        if count_1 == 0 and count_2 == 4:
            print('IP-адрес корректен')
            break