import os

file_to_delete = "backup_sample.txt"

if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
    print(f"Файл {file_to_delete} успешно удален.")
else:
    print(f"Файл {file_to_delete} не найден.")