source_file = "sample.txt"
target_file = "copied_sample.txt"

with open(source_file, "r", encoding="utf-8") as src:
    content = src.read()

with open(target_file, "w", encoding="utf-8") as dst:
    dst.write(content)

print(f"Содержимое из {source_file} успешно скопировано в {target_file}.")