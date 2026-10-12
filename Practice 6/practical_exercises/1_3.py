with open("sample.txt", "a", encoding="utf-8") as f:
    f.write("Line 3: Appended content\n")

with open("sample.txt", "r", encoding="utf-8") as f:
    updated_content = f.read()

print("Обновленное содержимое файла:")
print(updated_content)