import collections
import zipfile


def unzip(archive):
    zfile = zipfile.ZipFile(archive, 'r')
    for i_file_name in zfile.namelist():
        zfile.extract(i_file_name)
    zfile.close()


def collect_stats(file_name):
    if file_name.endswith('.zip'):
        unzip(file_name)
        file = ''.join((file_name[-3], 'txt'))
    result = {}
    text_file = open(file_name, 'r',  encoding='cp866') #CP866 или Windows-1251

    for i_line in text_file:
        for j_char in i_line:
            if j_char.isalpha():
                if j_char not in result:
                    result[j_char] = 0
                result[j_char] += 1
    text_file.close()

    return result


def print_stats(stats):
    print('+{:-^19}+'.format('+'))
    print('|{: ^9}|{: ^9}|'.format('буква', 'частота'))
    print('+{:-^19}+'.format('+'))
    for char, count in stats.items():
        print('|{: ^9}|{: ^9}|'.format(char, count))
    print('+{:-^19}+'.format('+'))


def sort_by_frequency(stats_dict):
    sorted_values = sorted(stats_dict.values(), reverse=True)
    sorted_dict = collections.OrderedDict()
    for i_value in sorted_values:
        for j_key in stats_dict.keys():
            if stats_dict[j_key] == i_value:
                sorted_dict[j_key] = stats_dict[j_key]

    return sorted_dict


file_name = 'voyna-i-mir.zip'
stats_data = collect_stats(file_name)

print_stats(sort_by_frequency(stats_data))
