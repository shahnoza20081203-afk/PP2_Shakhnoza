import os

python_files = [f for f in os.listdir(".") if f.endswith(".py")]

print("Найденные Python-файлы (.py):")
print(python_files)