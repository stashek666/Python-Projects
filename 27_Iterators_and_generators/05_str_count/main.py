import os
from collections.abc import Iterable


def gen_files_dir(path: str, depth=4) -> Iterable[str]:
    depth -= 1
    with os.scandir(path) as p:
        for entry in p:
            yield entry.path
            if entry.is_dir() and depth > 0:
                yield from gen_files_dir(entry.path, depth)


searching_path = 'C:\\python-ds'
files = list(gen_files_dir(path=searching_path))
line_count = 0

files_filtered = [x for x in files if x.endswith('.py')]
for file_dir in files_filtered:
    try:
        file = open(file_dir, "r")
        local_count = 0
        for line in file.read().split('\n'):
            if (not line.strip() == '') and \
                    (not line.strip().startswith("#")) and \
                    (not line.strip().startswith('"')):
                local_count += 1

        print('Путь к файлу: {} - {} строк'.format(file_dir, local_count))
        line_count += local_count
        file.close()
    except Exception:
        continue

print("=====================================")
print("Всего строк  - ", line_count)
