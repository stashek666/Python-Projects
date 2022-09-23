import os


def file_sizes(path):
    files_stat = [0, 0, 0]

    for i_elem in os.listdir(path):

        if os.path.isfile(os.path.abspath(
                os.path.join(path, i_elem))):
            file_path = os.path.abspath(
                os.path.join(path, i_elem))

            file_size = os.path.getsize(file_path)
            files_stat[0] += file_size
            files_stat[1] += 1

        else:
            result = file_sizes(os.path.abspath(
                os.path.join(path, i_elem)))
            files_stat[0] += result[0]
            files_stat[1] += result[1]
            files_stat[2] += 1

    return files_stat


main_path = os.path.abspath(
    os.path.join('..', '..', '23_Files'))

data = file_sizes(main_path)

print('Путь: ', main_path)
print('\nРазмер каталога (в Кб):', data[0] / 1024)
print('Количество подкаталогов:', data[2])
print('Количество файлов:', data[1])
