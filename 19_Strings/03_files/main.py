file_name = input('Введите название файла: ')
sym = '@', '№', '$', '%', '^', '&', '*', '()'
ext = '.txt', '.docx'

if file_name.startswith(sym):
    print('\nОшибка: название начинается на '
          'один из специальных символов')
elif not file_name.endswith(ext):
    print('\nОшибка: неверное расширение файла. '
         'Ожидалось .txt или .docx')
else:
    print('\nФайл назван верно.')