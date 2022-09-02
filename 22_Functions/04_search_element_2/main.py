def find_key(struct, key, depth):

    if key in struct:
        return struct[key]

    if depth > 1:
        for sub_struct in struct.values():
            if isinstance(sub_struct, dict):
                result = find_key(sub_struct, key, depth - 1)
                if result:
                    break
        else:
            result = None
        return result


site = {'html':
        {'head':
            {'title': 'Мой сайт'},
         'body': {'h2': 'Здесь будет мой заголовок',
                  'div': 'Тут, наверное, какой-то блок',
                  'p': 'А вот здесь новый абзац'
                  }
         }
        }


search_key = input('Искомый ключ: ').lower()
value = find_key(site, search_key, depth=5)

if value:
    print('\nИскомый ключ: ', value)
else:
    print('\nТакого ключа в структуре сайта нет.')


