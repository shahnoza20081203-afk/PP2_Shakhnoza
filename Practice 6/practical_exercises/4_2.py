import os

path = "sample.txt"

print(f"Проверка прав доступа для '{path}':")
print("Существует:", os.path.exists(path))
print("Доступен для чтения (R_OK):", os.access(path, os.R_OK))
print("Доступен для записи (W_OK):", os.access(path, os.W_OK))
print("Доступен для исполнения (X_OK):", os.access(path, os.X_OK))