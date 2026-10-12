import os

path = "my_folder/subfolder/file.txt"

if os.path.exists(path):
    print(f"Путь '{path}' существует.")
else:
    print(f"Путь '{path}' не существует, но мы всё равно можем его разделить:")

dir_portion, file_portion = os.path.split(path)

print("Директория:", dir_portion)
print("Имя файла:", file_portion)