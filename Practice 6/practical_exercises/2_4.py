import os
import shutil

os.makedirs("dir_source", exist_ok=True)
os.makedirs("dir_target", exist_ok=True)

source_file = os.path.join("dir_source", "data.txt")
with open(source_file, "w", encoding="utf-8") as f:
    f.write("Some test data")

shutil.copy(source_file, os.path.join("dir_target", "data_copy.txt"))

shutil.move(source_file, os.path.join("dir_target", "data.txt"))

print("Файлы успешно скопированы и перемещены.")