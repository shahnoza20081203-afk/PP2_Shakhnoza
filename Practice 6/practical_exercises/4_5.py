fruits = ["Apple", "Banana", "Cherry", "Orange"]

with open("fruits.txt", "w", encoding="utf-8") as f:
    for fruit in fruits:
        f.write(f"{fruit}\n")

print("Список успешно записан в fruits.txt.")