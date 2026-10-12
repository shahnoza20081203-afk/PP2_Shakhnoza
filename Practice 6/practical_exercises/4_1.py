import os

path = "."

all_entries = os.listdir(path)

only_files = [f for f in all_entries if os.path.isfile(os.path.join(path, f))]
only_dirs = [d for d in all_entries if os.path.isdir(os.path.join(path, d))]

print("Только папки:", only_dirs)
print("Только файлы:", only_files)
print("Все объекты:", all_entries)