filename = "sample.txt"

with open(filename, "r", encoding="utf-8") as f:
    lines = f.readlines()
    line_count = len(lines)

print(f"Количество строк в файле {filename}: {line_count}")