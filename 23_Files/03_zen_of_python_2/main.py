import string

file = open(r'C:\python-ds\23_Files\02_zen_of_python\zen.txt')

file_read = file.read()
file_words = file_read.split()
file_rls = file_read.split('\n')
chars = [i for i in file_read if i in string.ascii_letters]

print(f'Количество букв в файле: {len(chars)}')
print(f'Количество слов в файле: {len(file_words)}')
print(f'Количество строк в файле: {len(file_rls)}')
print(f'Наиболее редкая буква: {min(chars, key=lambda x: file_read.count(x))}')
file.close()
