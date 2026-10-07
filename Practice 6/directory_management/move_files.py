import os
import shutil

dir_a = "dir_a"
dir_b = "dir_b"

os.makedirs(dir_a, exist_ok=True)
os.makedirs(dir_b, exist_ok=True)

file_name = "test_move.txt"
file_in_a = os.path.join(dir_a, file_name)

with open(file_in_a, "w", encoding="utf-8") as f:
    f.write("Moving file exercise.\n")

moved_file = shutil.move(file_in_a, os.path.join(dir_b, file_name))
print(f"Moved file to: {moved_file}")

# Очистка
os.remove(moved_file)
os.rmdir(dir_a)
os.rmdir(dir_b)