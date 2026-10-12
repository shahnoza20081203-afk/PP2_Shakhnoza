import os
import string

output_dir = "alphabet_files"
os.makedirs(output_dir, exist_ok=True)

for letter in string.ascii_uppercase:
    file_path = os.path.join(output_dir, f"{letter}.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"Это файл {letter}.txt\n")

print(f"Сгенерировано 26 файлов в директории {output_dir}/.")