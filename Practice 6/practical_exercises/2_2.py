import os

items = os.listdir(".")
print("Элементы в текущей директории:")
for item in items:
    print(item)