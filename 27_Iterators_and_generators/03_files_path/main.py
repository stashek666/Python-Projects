import os
from collections.abc import Iterable


def gen_files_path(dir_name: str, path: str) -> Iterable[str]:
    print('Текущий путь: ', path)
    for i_elem in os.listdir(path):
        current_path = os.path.join(path, i_elem)
        if os.path.isdir(current_path) and i_elem != dir_name:
            gen_files_path(dir_name, current_path)
        elif os.path.isfile(os.path.join(path, i_elem)):
            yield os.path.join(path, i_elem)


directory = 'SkillBox'
abs_path = os.path.abspath(os.path.join(os.path.sep))
res = gen_files_path(dir_name=directory, path=abs_path)

for i in res:
    print(i)
