import os
import string

filename = "output.txt"

with open(filename, "w", encoding="utf-8") as f:
    f.write("Initial line 1\nInitial line 2\n")

with open(filename, "a", encoding="utf-8") as f:
    f.write("Appended line 3\nAppended line 4\n")

data_list = ["Apple", "Banana", "Cherry", "Date"]
list_file = "fruits.txt"
with open(list_file, "w", encoding="utf-8") as f:
    for item in data_list:
        f.write(f"{item}\n")

output_dir = "letters_files"
os.makedirs(output_dir, exist_ok=True)
for letter in string.ascii_uppercase:
    file_path = os.path.join(output_dir, f"{letter}.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"This is file {letter}.txt\n")

print(f"Generated 26 files in '{output_dir}/'")

os.remove(filename)
os.remove(list_file)
for letter in string.ascii_uppercase:
    os.remove(os.path.join(output_dir, f"{letter}.txt"))
os.rmdir(output_dir)